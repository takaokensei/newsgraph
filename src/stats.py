from neo4j import GraphDatabase
from src.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def generate_stats():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    stats = {}
    
    with driver.session() as session:
        # 1. Total Counts
        stats['Nodes'] = session.run("MATCH (n) RETURN count(n) as c").single()['c']
        stats['Relationships'] = session.run("MATCH ()-[r]->() RETURN count(r) as c").single()['c']
        
        # 2. Nodes by Category
        result = session.run("MATCH (n:Entity) RETURN n.category as Category, count(n) as Count ORDER BY Count DESC")
        stats['By Category'] = pd.DataFrame([r.data() for r in result])
        
        # 3. Top Connected Entities (Degree Centrality equivalent)
        query = """
        MATCH (n)-[r]-()
        RETURN n.name as Entity, n.type as Type, count(r) as Degree
        ORDER BY Degree DESC LIMIT 10
        """
        result = session.run(query)
        stats['Top Entities'] = pd.DataFrame([r.data() for r in result])
        
        # 4. Most Common Relations
        query = """
        MATCH ()-[r]->()
        RETURN type(r) as Relation, count(r) as Count
        ORDER BY Count DESC LIMIT 10
        """
        result = session.run(query)
        stats['Top Relations'] = pd.DataFrame([r.data() for r in result])

    driver.close()
    
    print("\n" + "="*40)
    print("📊 NEWSGRAPH STATISTICS REPORT")
    print("="*40)
    print(f"\nTotal Nodes: {stats['Nodes']}")
    print(f"Total Relationships: {stats['Relationships']}")
    
    print("\n🔹 Nodes by Category:")
    print(stats['By Category'].to_string(index=False))
    
    print("\n🔹 Top 10 Most Connected Entities:")
    print(stats['Top Entities'].to_string(index=False))
    
    print("\n🔹 Top 10 Relationship Types:")
    print(stats['Top Relations'].to_string(index=False))
    print("\n" + "="*40)

if __name__ == "__main__":
    generate_stats()
