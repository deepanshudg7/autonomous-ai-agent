"""SQLite-based persistent memory tool for the agent."""

import sqlite3
from langchain_core.tools import tool

DB_PATH = "agent_memory.db"


def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS memory (key TEXT PRIMARY KEY, value TEXT)")
    return conn


@tool
def save_memory(key: str, value: str) -> str:
    """Save a key-value pair to persistent memory."""
    with _get_conn() as conn:
        conn.execute("INSERT OR REPLACE INTO memory (key, value) VALUES (?, ?)", (key, value))
    return f"Saved: {key}"


@tool
def recall_memory(key: str) -> str:
    """Recall a value from persistent memory by key."""
    with _get_conn() as conn:
        row = conn.execute("SELECT value FROM memory WHERE key = ?", (key,)).fetchone()
    return row[0] if row else f"No memory found for key: {key}"
