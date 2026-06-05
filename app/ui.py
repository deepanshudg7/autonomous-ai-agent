"""Streamlit UI for Autonomous AI Agent."""

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from app.agent import build_agent
from app.providers import get_provider

load_dotenv()

st.set_page_config(page_title="🤖 Autonomous Agent", layout="wide")
st.title("🤖 Autonomous AI Agent")
provider = get_provider()
model = os.getenv("LLM_MODEL", "llama3.2" if provider == "ollama" else "gpt-4o-mini")
st.caption(f"Provider: **{provider.upper()}** | Model: **{model}** | Tools: Search, Code Exec, Memory")

if "agent" not in st.session_state:
    with st.spinner("Initializing agent..."):
        st.session_state.agent = build_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if task := st.chat_input("Give the agent a task..."):
    st.session_state.messages.append({"role": "user", "content": task})
    with st.chat_message("user"):
        st.markdown(task)

    with st.chat_message("assistant"):
        with st.spinner("Agent working..."):
            result = st.session_state.agent.invoke({"messages": [HumanMessage(content=task)]})
            response = result["messages"][-1].content
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
