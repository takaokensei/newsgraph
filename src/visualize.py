import networkx as nx
import matplotlib.pyplot as plt
from neo4j import GraphDatabase
from src.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_static_graph(limit=100):
    """
    Fetch data from Neo4j and generate a static image using NetworkX.
    """
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    
    G = nx.DiGraph()
    
    query = f"""
    MATCH (n)-[r]->(m)
    RETURN n.name as source, type(r) as relation, m.name as target, n.category as category
    LIMIT {limit}
    """
    
    logger.info(f"Fetching graph data (Limit: {limit})...")
    
    try:
        with driver.session() as session:
            result = session.run(query)
            for record in result:
                source = record['source']
                target = record['target']
                relation = record['relation']
                category = record.get('category', 'Unknown')
                
                G.add_edge(source, target, label=relation)
                # Store category as node attribute for coloring
                if source not in G.nodes:
                    G.nodes[source]['category'] = category
                
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        driver.close()
        return

    driver.close()
    
    if G.number_of_nodes() == 0:
        logger.warning("No nodes found to visualize.")
        return

    logger.info(f"Generating visualization for {G.number_of_nodes()} nodes and {G.number_of_edges()} edges...")
    
    # Tokyo Night Colors
    BG_COLOR = '#1a1b26'
    NODE_COLOR = '#7aa2f7' # Blue accent
    EDGE_COLOR = '#414868' # Muted blue-grey
    TEXT_COLOR = '#c0caf5' # White-ish
    CATEGORY_COLORS = {
        'Economia': '#9ece6a', # Green
        'Esportes': '#f7768e', # Red
        'Política': '#bb9af7', # Purple
        'Turismo': '#7dcfff', # Cyan
        'Variedades e Sociedade': '#e0af68', # Orange
        'Polícia e Direitos': '#ff9e64' # Orange-Red
    }

    plt.figure(figsize=(24, 18), facecolor=BG_COLOR)
    ax = plt.gca()
    ax.set_facecolor(BG_COLOR)
    
    # Layout - Increase k for more spacing
    pos = nx.spring_layout(G, k=0.5, iterations=200, seed=42)
    
    # Node Sizing by Degree
    degrees = dict(G.degree())
    # Normalize sizes
    node_sizes = [v * 150 + 500 for v in degrees.values()]
    
    # Node Colors by Category
    node_colors = [CATEGORY_COLORS.get(G.nodes[n].get('category', ''), NODE_COLOR) for n in G.nodes()]

    # Draw Edges (Curved for aesthetics)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.4, edge_color=EDGE_COLOR, 
                           arrowstyle='-|>', arrowsize=10, connectionstyle='arc3,rad=0.1')

    # Draw Nodes
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9, edgecolors='#16161e')
    
    # Draw Labels with Background for Readability
    labels = {n: n for n, d in degrees.items() if d > 0}
    
    # Draw labels with a box/halo
    text_items = nx.draw_networkx_labels(G, pos, labels, font_size=9, font_family='sans-serif', font_color=TEXT_COLOR, font_weight='bold')
    
    # Add halo/background to text
    for _, t in text_items.items():
        t.set_bbox(dict(facecolor=BG_COLOR, edgecolor='none', alpha=0.6, boxstyle='round,pad=0.2'))

    plt.title("NewsGraph Knowledge Graph (Tokyo Night Theme)", color=TEXT_COLOR, fontsize=24, pad=20)
    plt.axis('off')
    
    # Save to Artifacts Directory
    output_path = r"C:\Users\Cauã V\.gemini\antigravity\brain\88df315f-eb1c-4ac5-8003-b70dd25c0f37\images\knowledge_graph_tokyo.png"
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor=BG_COLOR)
    logger.info(f"Graph saved to {output_path}")
    plt.close()

if __name__ == "__main__":
    generate_static_graph(limit=150)
