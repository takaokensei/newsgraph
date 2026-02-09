from neo4j import GraphDatabase
from src.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

def verify_graph():
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    with driver.session() as session:
        # Count Nodes
        result = session.run("MATCH (n) RETURN count(n) as count")
        node_count = result.single()["count"]
        
        # Count Relations
        result = session.run("MATCH ()-[r]->() RETURN count(r) as count")
        rel_count = result.single()["count"]
        
        print(f"📊 Graph Status:")
        print(f"   - Nodes: {node_count}")
        print(f"   - Relationships: {rel_count}")
        
        # Sample Data
        print("\n🔍 Sample Nodes:")
        result = session.run("MATCH (n) RETURN n.name, n.type, n.category LIMIT 5")
        for record in result:
            print(f"   - {record['n.name']} ({record['n.type']}) [{record['n.category']}]")

    driver.close()

if __name__ == "__main__":
    verify_graph()
