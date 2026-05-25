# LangGraph Learning and Implementation

This repository contains my hands-on work while studying LangGraph, LangChain, LangSmith, RAG, MCP, and Streamlit-based chatbot development. It starts with small graph workflow notebooks and progresses into practical agentic chatbot systems with memory, tools, human approval, document retrieval, tracing, and MCP integration.

## What I Covered

- LangGraph state, nodes, edges, graph compilation, and invocation
- Sequential workflows, conditional routing, parallel execution, and subgraphs
- Tool-calling agents using `ToolNode`, `tools_condition`, web search, calculator, and stock lookup
- Memory and persistence using in-memory and SQLite checkpointers
- Human-in-the-loop workflows using interrupt/resume
- PDF RAG using PyPDFLoader, chunking, OpenAI embeddings, and FAISS
- LangSmith tracing for LLM calls, RAG pipelines, agents, and LangGraph runs
- MCP servers and MCP-enabled chatbot integration
- Streamlit chat interfaces with threaded conversations and persistent history

## Main Work

### Foundational LangGraph Notebooks

- `BMI_Workflow.ipynb`
- `Quadratic_workflow.ipynb`
- `Batsman_workflow.ipynb`
- `Simple_llm_workflow.ipynb`
- `prompt_chaining.ipynb`
- `review_reply_workflow.ipynb`
- `X_post_generator.ipynb`
- `Subgraphs.ipynb`
- `Shared_Subgraph.ipynb`
- `persistence.ipynb`
- `Human_In_The_Loop.ipynb`
- `UPSC_Essay_Workflow.ipynb`
- `tools.ipynb`

### Chatbot Applications

The `Chatbot/` folder contains multiple Streamlit chatbot versions:

- Basic chatbot backend and frontend
- SQLite-persistent threaded chatbot
- Tool-using chatbot
- PDF RAG chatbot
- MCP-enabled chatbot

### LangSmith Experiments

The `LangSmith/` folder contains experiments for:

- Simple LLM calls
- Sequential chains
- PDF RAG pipelines
- Traced setup and query runs
- Cached FAISS vector indexes
- ReAct agents
- LangGraph-based essay evaluation

### MCP Work

The `MCP/` folder contains an expense-tracking MCP server backed by SQLite.

The `manim-mcp-server/` folder contains a Manim MCP server that can execute Manim code and generate animation videos.

## Example Commands

Install dependencies as needed, then run the Streamlit apps from the repository root:

```bash
streamlit run Chatbot/frontend.py
streamlit run Chatbot/frontend_threading.py
streamlit run Chatbot/frontend_tool.py
streamlit run Chatbot/frontend_rag.py
streamlit run Chatbot/frontend_mcp.py
```

Run the human-in-the-loop CLI demo:

```bash
python chatbot_HITL.py
```

Run the local expense MCP server:

```bash
python MCP/main.py
```


