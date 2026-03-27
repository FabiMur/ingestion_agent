from strands import tool
from ddgs import DDGS


@tool
def web_search(query: str) -> str:
    """Performs a web search using DuckDuckGo and returns the results."""
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=5)
        return "\n".join(results)
    except Exception as e:
        return f"Error performing web search: {e}"
