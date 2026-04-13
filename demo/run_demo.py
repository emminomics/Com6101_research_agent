from tools.paper_search import search_papers
from tools.pdf_summarizer import summarize_pdf
from memory.buffer import MemoryBuffer

def run_demo():
    mem = MemoryBuffer(max_turns=5)

    # Step 1: User asks for papers
    user_query = "neural networks"
    mem.add("user", f"Find papers on {user_query}")
    papers = search_papers(user_query, 2)
    mem.add("agent", f"Found {len(papers)} papers")

    # Step 2: Show paper titles
    print("\n--- Papers Found ---")
    for i, p in enumerate(papers, 1):
        print(f"{i}. {p['title']} ({', '.join(p['authors'])})")
        print(f"Link: {p['link']}\n")

    # Step 3: User asks to summarize a PDF
    mem.add("user", "Summarize sample.pdf")
    summary = summarize_pdf("sample.pdf", 300)
    mem.add("agent", "Here is the summary of sample.pdf")

    print("\n--- PDF Summary ---")
    print(summary)

    # Step 4: Show memory context
    print("\n--- Conversation Context ---")
    print(mem.get_context())

if __name__ == "__main__":
    run_demo()
