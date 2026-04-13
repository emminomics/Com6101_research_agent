import requests

def search_papers(query: str, max_results: int = 5):
    """
    Search academic papers from arXiv API.
    Args:
        query (str): Search keywords
        max_results (int): Number of papers to return
    Returns:
        list of dict: Each dict contains title, authors, summary, link
    """
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"
    response = requests.get(url)

    if response.status_code != 200:
        return [{"error": "Failed to fetch papers"}]

    # Parse XML response
    import xml.etree.ElementTree as ET
    root = ET.fromstring(response.text)

    papers = []
    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()
        link = entry.find("{http://www.w3.org/2005/Atom}id").text.strip()
        authors = [author.find("{http://www.w3.org/2005/Atom}name").text for author in entry.findall("{http://www.w3.org/2005/Atom}author")]

        papers.append({
            "title": title,
            "authors": authors,
            "summary": summary,
            "link": link
        })

    return papers
