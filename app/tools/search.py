"""Web search tool via Tavily."""

import os
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()


def get_search_tool():
    return TavilySearchResults(max_results=5, api_key=os.getenv("TAVILY_API_KEY"))
