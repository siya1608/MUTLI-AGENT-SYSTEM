import os
from langchain_core.tools import tool
from tavily import TavilyClient
import requests
from bs4 import BeautifulSoup

@tool
def tavily_search(query: str) -> list:
    """Search the web for queries using Tavily. Returns a list of dictionaries with 'title', 'url', and 'content'."""
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        return [{"error": "TAVILY_API_KEY environment variable is not set."}]
    try:
        client = TavilyClient(api_key=tavily_api_key)
        response = client.search(query=query, max_results=5)
        results = response.get("results", [])
        return [{"title": r.get("title"), "url": r.get("url"), "content": r.get("content")} for r in results]
    except Exception as e:
        return [{"error": f"Failed to perform search: {str(e)}"}]

@tool
def scrape_webpage(url: str) -> str:
    """Scrape a webpage given its URL using BeautifulSoup and extract readable text."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        
        for script in soup(["script", "style", "header", "footer", "nav"]):
            script.decompose()
            
        text = soup.get_text(separator="\n")
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = "\n".join(chunk for chunk in chunks if chunk)
        
        return text_content[:5000]
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"
