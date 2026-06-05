"""Resolve LLM provider based on LLM_PROVIDER env variable."""

import os
from dotenv import load_dotenv

load_dotenv()


def get_provider() -> str:
    return os.getenv("LLM_PROVIDER", "ollama").lower()


def get_llm():
    provider = get_provider()
    model = os.getenv("LLM_MODEL")
    if provider == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(
            model=model or "llama3.2",
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            temperature=0,
        )
    elif provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model or "gpt-4o-mini", temperature=0)
    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: '{provider}'")
