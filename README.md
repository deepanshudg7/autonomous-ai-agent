# 🤖 Autonomous AI Agent

An autonomous AI agent built with LangGraph that plans, executes, reflects, and retries using tools like web search, code execution, and database access.

## 🧱 Stack
- **LangGraph** – ReAct agent loop with state management
- **Ollama / OpenAI** – LLM backbone
- **Tavily** – web search tool
- **Python REPL** – code execution tool
- **SQLite** – persistent memory/database tool
- **Streamlit** – UI

## 🗂️ Project Structure
```
autonomous-ai-agent/
├── app/
│   ├── tools/
│   │   ├── search.py       # Web search via Tavily
│   │   ├── code_exec.py    # Python code executor
│   │   └── memory.py       # SQLite-based memory tool
│   ├── agent.py            # LangGraph ReAct agent definition
│   ├── providers.py        # LLM provider resolver
│   └── ui.py               # Streamlit UI
├── .env.example
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

```bash
git clone https://github.com/deepanshudg7/autonomous-ai-agent.git
cd autonomous-ai-agent
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app/ui.py
```

## 🔑 Environment Variables
| Variable | Description |
|---|---|
| `LLM_PROVIDER` | `ollama` (default) or `openai` |
| `LLM_MODEL` | e.g. `llama3.2` or `gpt-4o-mini` |
| `OLLAMA_BASE_URL` | Ollama server URL |
| `OPENAI_API_KEY` | Required if using OpenAI |
| `TAVILY_API_KEY` | Required for web search tool |
