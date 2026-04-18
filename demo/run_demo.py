from tools.paper_search import search_papers
from tools.pdf_summarizer import summarize_pdf
from memory.buffer import MemoryBuffer
import requests
import os
import sys

def download_pdf(url, save_path="downloaded.pdf"):
    response = requests.get(url)
    response.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(response.content)
    return save_path

#def run_demo():
    #mem = MemoryBuffer(max_turns=5)

    # Step 1: User asks for papers
    #user_query = "Fashion-MNIST"
    #mem.add("user", f"Find papers on {user_query}")
    #papers = search_papers(user_query, 2)
    #mem.add("agent", f"Found {len(papers)} papers")

   

def run_demo():
    mem = MemoryBuffer(max_turns=5)

    # Step 1: User asks for papers
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = "Fashion-MNIST"

    mem.add("user", f"Find papers on {user_query}")
    papers = search_papers(user_query, 2)
    ...


    # Step 2: Show paper titles
    print("\n--- Papers Found ---")
    for i, p in enumerate(papers, 1):
        print(f"{i}. {p['title']} ({', '.join(p['authors'])})")
        print(f"Link: {p['link']}\n")

    # Step 3: Automatically download the first paper’s PDF
    first_link = papers[0]['link'].replace("abs", "pdf")  # arXiv trick
    import re

    # Clean the paper title to make a safe filename
    safe_title = re.sub(r'\W+', '_', papers[0]['title'])[:50]  # limit length
    pdf_path = download_pdf(first_link, f"docs/{safe_title}.pdf")
    
    #pdf_path = download_pdf(first_link, "docs/fashion_mnist.pdf")

    mem.add("user", f"Summarize {pdf_path}")
    summary = summarize_pdf(pdf_path, 300)
    mem.add("agent", f"Here is the summary of {pdf_path}")

    print("\n--- PDF Summary ---")
    print(summary)

    # Step 4: Show memory context
    print("\n--- Conversation Context ---")
    print(mem.get_context())

if __name__ == "__main__":
    run_demo()
