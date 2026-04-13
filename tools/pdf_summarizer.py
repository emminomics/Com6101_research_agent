import fitz  # PyMuPDF

def summarize_pdf(file_path: str, max_chars: int = 1000):
    """
    Summarize a PDF file by extracting text and truncating.
    Args:
        file_path (str): Path to the PDF file
        max_chars (int): Maximum characters to include in summary
    Returns:
        str: Summary text
    """
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        # Simple summarization: truncate text
        summary = text[:max_chars]
        return summary.strip()

    except Exception as e:
        return f"Error reading PDF: {e}"
