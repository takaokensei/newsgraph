from neo4j import GraphDatabase
import logging
from typing import List, Dict, Any
from src.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

logger = logging.getLogger(__name__)

class GraphBuilder:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    def close(self):
        self.driver.close()

    def verify_connection(self):
        try:
            with self.driver.session() as session:
                result = session.run("RETURN 1 AS num")
                record = result.single()
                if record and record["num"] == 1:
                    logger.info("✅ Connected to Neo4j successfully.")
                    return True
        except Exception as e:
            logger.error(f"❌ Failed to connect to Neo4j: {e}")
            return False

    def create_graph_from_triplets(self, triplets: Dict[str, Any], category: str):
        """
        Ingest extracted entities and relationships into Neo4j.
        """
        entities = triplets.get("entities", [])
        relationships = triplets.get("relationships", [])
        
        with self.driver.session() as session:
            # 1. Create Entities
            for entity in entities:
                query = """
                MERGE (e:Entity {name: $name})
                SET e.type = $type, e.category = $category
                RETURN e
                """
                session.run(query, name=entity["name"], type=entity["type"], category=category)
            
            # 2. Create Relationships
            for rel in relationships:
                query = """
                MATCH (s:Entity {name: $source})
                MATCH (t:Entity {name: $target})
                MERGE (s)-[r:RELATION {type: $relation}]->(t)
                RETURN r
                """
                # Neo4j relationship types cannot be dynamic parameters easily in MERGE without APOC or specific syntax.
                # For simplicity/safety, we might sanitize the relation type or use APOC.
                # Here, we'll try to use APOC if available, or just string formatting (careful with injection).
                # Safer approach:
                safe_rel_type = "".join(x for x in rel["relation"] if x.isalnum() or x == "_").upper()
                
                query = f"""
                MATCH (s:Entity {{name: $source}})
                MATCH (t:Entity {{name: $target}})
                MERGE (s)-[r:{safe_rel_type}]->(t)
                RETURN r
                """
                
                try:
                    session.run(query, source=rel["source"], target=rel["target"])
                except Exception as e:
                    logger.error(f"Failed to create relationship {rel}: {e}")

            logger.info(f"Inserted {len(entities)} nodes and {len(relationships)} relationships for category '{category}'")
