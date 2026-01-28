def chunk_text(text, chunk_size=120, overlap=30):
    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks

"""
NOTE ON CHUNKING:

Although the demo data appears short or pre-chunked, chunking is still an
explicit step to illustrate how real financial documents are handled.

In production, documents like 10-Ks, earnings calls, and research notes are
long and must be split into semantically coherent chunks to:
- Stay within LLM context limits
- Improve retrieval precision
- Enable explainable, citation-backed answers

Chunk size and overlap are key quality levers in finance-focused RAG systems.
"""

