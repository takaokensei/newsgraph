# 📰 NewsGraph

**Uma Pipeline de Extração de Conhecimento e Grafo para Notícias (RAG + Graph)**

![Graph Visualization](images/knowledge_graph_tokyo.png)

## 📌 Sobre o Projeto
O **NewsGraph** é um sistema que processa notícias não estruturadas, extrai Entidades e Relacionamentos usando Large Language Models (LLMs) locais e constrói um Grafo de Conhecimento em Neo4j.

O objetivo é permitir consultas complexas e insights que vão além da busca semântica tradicional.

## 🚀 Tecnologias
- **Python 3.12**
- **Neo4j** (Banco de Dados em Grafo)
- **Ollama / Llama 3** (Extração de Conhecimento Local)
- **Docker** (Infraestrutura)
- **LangChain** (Orquestração)

## 🛠️ Instalação e Uso

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/takaokensei/newsgraph.git
    cd newsgraph
    ```

2.  **Inicie a Infraestrutura (Neo4j):**
    ```bash
    docker-compose up -d
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure o LLM:**
    - Certifique-se de que o [Ollama](https://ollama.com/) está rodando (`ollama serve`).
    - Modelo padrão: `llama3`.

5.  **Execute o Pipeline:**
    ```bash
    python main.py
    ```

## 📊 Estatísticas (Base Completa - 319 Artigos)
- **Nós Extraídos:** 907
- **Relacionamentos:** 755
- **Sucesso na Ingestão:** 99.7%

## 📂 Estrutura do Projeto
- `src/ingestion.py`: Carregamento e limpeza de dados.
- `src/llm_extraction.py`: Engenharia de Prompt e extração JSON.
- `src/graph_builder.py`: Ingestão no Neo4j.
- `src/visualize.py`: Geração de visualizações (Matplotlib/NetworkX).
- `src/stats.py`: Relatórios estatísticos.

---
Desenvolvido por **Cauã Vitor**.
