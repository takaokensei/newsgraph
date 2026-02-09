<div align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=1a1b26&height=120&section=header"/>
  
  <h1>
    <img src="https://readme-typing-svg.herokuapp.com/?lines=📰+NEWSGRAPH;Knowledge+Graph+Extraction;RAG+Architecture;Local+LLM+Pipeline&font=Fira+Code&center=true&width=600&height=50&color=7aa2f7&vCenter=true&pause=1000&size=28" />
  </h1>
  
  <samp>Structure Unstructured Data · GraphRAG Ready · Local Privacy</samp>
  <br/><br/>
  
  <img src="https://img.shields.io/badge/Python-3.12+-c0caf5?style=for-the-badge&logo=python&logoColor=1a1b26"/>
  <img src="https://img.shields.io/badge/Neo4j-GraphDB-7aa2f7?style=for-the-badge&logo=neo4j&logoColor=1a1b26"/>
  <img src="https://img.shields.io/badge/Ollama-Llama3-9ece6a?style=for-the-badge&logo=ollama&logoColor=1a1b26"/>
  <img src="https://img.shields.io/badge/Docker-Container-bb9af7?style=for-the-badge&logo=docker&logoColor=1a1b26"/>
  <img src="https://img.shields.io/badge/Status-Completed-9ece6a?style=for-the-badge"/>
</div>

<br/>



## `> tech_stack`

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,docker,neo4j,linux,git&theme=dark&perline=7" />
</div>

<table align="center">
<tr>
<td align="center" width="33%">
<strong>⚙️ Core Engine</strong><br/><br/>
<img src="https://img.shields.io/badge/Python-3.12-c0caf5?style=flat-square&logo=python&logoColor=1a1b26"/>
<img src="https://img.shields.io/badge/LangChain-Orchestration-7aa2f7?style=flat-square"/>
<img src="https://img.shields.io/badge/Pydantic-Validation-9ece6a?style=flat-square"/>
</td>
<td align="center" width="33%">
<strong>🕸️ Data & Graph</strong><br/><br/>
<img src="https://img.shields.io/badge/Neo4j-5.15-bb9af7?style=flat-square&logo=neo4j&logoColor=1a1b26"/>
<img src="https://img.shields.io/badge/Cypher-Query_Lang-7dcfff?style=flat-square"/>
<img src="https://img.shields.io/badge/Pandas-Data_Processing-1a1b26?style=flat-square&logo=pandas&logoColor=white"/>
</td>
<td align="center" width="33%">
<strong>🧠 AI & Extraction</strong><br/><br/>
<img src="https://img.shields.io/badge/Ollama-Local_Inference-9ece6a?style=flat-square"/>
<img src="https://img.shields.io/badge/Llama_3-8B-f7768e?style=flat-square"/>
<img src="https://img.shields.io/badge/JSON_Mode-Structured_Output-c0caf5?style=flat-square"/>
</td>
</tr>
</table>

<br/>

## `> architecture_overview`

```
newsgraph/
│
├── 🐍 src/                    # Python Source Code
│   ├── ingestion.py           # CSV Loading & pre-processing
│   ├── llm_extraction.py      # Prompt Engineering & JSON Parsing
│   ├── graph_builder.py       # Neo4j Driver & Cypher Injection
│   ├── visualize.py           # NetworkX/Matplotlib Visualization
│   └── stats.py               # Statistical Analysis
│
├── 🐳 docker-compose.yml      # Neo4j Infrastructure
├── 📄 requirements.txt        # Python Dependencies
└── 📓 main.py                 # Orchestration Pipeline
```

<br/>

## `> workflow_pipeline`

<table align="center">
<tr>
<td width="50%">
<h3 align="center">📥 Phase 1: Ingestion</h3>
<p align="center">
<img src="https://img.shields.io/badge/Status-✅_Complete-9ece6a?style=for-the-badge"/>
</p>

**Input:** Raw CSV Dataset (319 Articles)
**Process:**
1. Clean text (remove artifacts)
2. Filter valid categories
3. Batch processing preparation

</td>
<td width="50%">
<h3 align="center">🧠 Phase 2: AI Extraction</h3>
<p align="center">
<img src="https://img.shields.io/badge/Status-✅_Complete-9ece6a?style=for-the-badge"/>
</p>

**Process:**
1. Prompt Llama 3 with rigorous JSON schema
2. Extract Entities (Person, Org, Location, Concept)
3. Extract Relationships (VERB_BASED)
4. Handle LLM hallucinations/formatting errors

</td>
</tr>
<tr>
<td width="50%">
<h3 align="center">🟢 Phase 3: Graph Construction</h3>
<p align="center">
<img src="https://img.shields.io/badge/Status-✅_Complete-9ece6a?style=for-the-badge"/>
</p>

**Technology:** Neo4j (Bolt Protocol)
**Logic:**
- `MERGE` nodes to avoid duplicates
- Connect entities with directional relationships
- Assign categories as Node Labels

</td>
<td width="50%">
<h3 align="center">📊 Phase 4: Viz & Stats</h3>
<p align="center">
<img src="https://img.shields.io/badge/Status-✅_Complete-9ece6a?style=for-the-badge"/>
</p>

**Output:** High-res Generation
**Stats:**
- **907** Unique Nodes
- **755** Semantic Relationships
- **Tokyo Night** Themed Visualization

</td>
</tr>
</table>

<br/>

## `> graph_statistics`

<div align="center">
<img src="https://img.shields.io/badge/Dataset-319_Articles-f7768e?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Nodes-907-7aa2f7?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Relations-755-bb9af7?style=for-the-badge"/>
</div>

**Top Connected Entities:**
1. **Brasil** (Location) - *Hub Central*
2. **Tecnologia** (Concept) - *Cross-cutting theme*
3. **Economia** (Concept)
4. **Startups** (Organization)

**Visualization Preview:**
<div align="center">
  <img src="images/knowledge_graph_tokyo.png" width="80%" style="border-radius: 10px; border: 2px solid #7aa2f7;" />
</div>

<br/>

## `> installation`

```bash
# 1. Clone the repository
git clone https://github.com/takaokensei/newsgraph.git
cd newsgraph

# 2. Start Infrastructure (Neo4j)
docker-compose up -d

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Setup Local LLM (Ollama)
ollama serve
ollama pull llama3

# 5. Run the Pipeline
python main.py
```

<br/>

## `> contact`

<div align="center">
  
  <strong>Cauã Vitor (takaokensei)</strong>
  <br/>
  <samp>AI Engineer & Researcher</samp>
  <br/>
  <samp>UFRN - Electrical Engineering</samp>
  
  <br/><br/>
  
  <a href="https://github.com/takaokensei">
    <img src="https://img.shields.io/badge/-GitHub-1a1b26?style=for-the-badge&logo=github&logoColor=c0caf5"/>
  </a>
</div>

<br/>

<div align="center">
  <img src="https://img.shields.io/badge/Made_with-Python_🐍-c0caf5?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Powered_by-Neo4j-7aa2f7?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Theme-Tokyo_Night-bb9af7?style=for-the-badge"/>
</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=1a1b26&height=100&section=footer"/>
