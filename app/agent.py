"""LangGraph ReAct autonomous agent."""

from langgraph.prebuilt import create_react_agent
from app.providers import get_llm
from app.tools.search import get_search_tool
from app.tools.code_exec import execute_python
from app.tools.memory import save_memory, recall_memory


def build_agent():
    llm = get_llm()
    tools = [get_search_tool(), execute_python, save_memory, recall_memory]
    return create_react_agent(llm, tools)
