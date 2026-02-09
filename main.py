import sys
import logging
from src.ingestion import load_data
from src.llm_extraction import LLMExtractor, MockExtractor
from src.graph_builder import GraphBuilder
from src.config import LLM_PROVIDER

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    # 1. Load Data
    df = load_data()
    if df is None:
        logger.error("Failed to load data. Exiting.")
        return

    # 2. Initialize Components
    try:
        # Check LLM connection (or drop to Mock)
        # For now, we assume user might want to force Mock if LLM isn't ready
        # But per plan, we try to use the configured provider.
        extractor = LLMExtractor() 
    except Exception as e:
        logger.warning(f"Failed to initialize LLM ({e}). Switching to Mock Extractor for demonstration.")
        extractor = MockExtractor()

    graph_builder = GraphBuilder()
    
    # 3. Verify Graph Connection
    if not graph_builder.verify_connection():
        logger.error("Neo4j is not accessible. Please start the Docker container.")
        # Proceeding might be useless, but we can verify extraction logic at least.
        # return 
    
    # 4. Processing Loop (Full Dataset)
    logger.info(f"Processing FULL dataset ({len(df)} articles)...")
    
    # Use tqdm if available, otherwise just loop
    try:
        from tqdm import tqdm
        iterator = tqdm(df.iterrows(), total=len(df), desc="Processing Articles")
    except ImportError:
        iterator = df.iterrows()
        logger.info("tqdm not found, using simple iterator")

    success_count = 0
    failure_count = 0

    for index, row in iterator:
        text = row['Texto Expandido']
        category = row['Categoria']
        
        try:
            # Extract
            triplets = extractor.extract_triplets(text, category)
            
            # Ingest
            if graph_builder.verify_connection():
                graph_builder.create_graph_from_triplets(triplets, category)
                success_count += 1
            else:
                logger.warning("Skipping Neo4j ingestion (Not connected).")
                failure_count += 1
                
        except Exception as e:
            logger.error(f"Error processing article {index}: {e}")
            failure_count += 1

    graph_builder.close()
    logger.info(f"Pipeline completed. Success: {success_count}, Failures: {failure_count}")

if __name__ == "__main__":
    main()
