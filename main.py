from data.documents import DOCUMENTS
from utils.chunking import chunk_text
from embeddings.embedder import embed_text
from retrieval.vector_store import VectorStore
from rag.qa import answer_question

# Step 1: Chunk documents
all_chunks = []
for doc in DOCUMENTS:
    chunks = chunk_text(doc["text"])
    all_chunks.extend(chunks)

# Step 2: Embed chunks
embeddings = embed_text(all_chunks)

# Step 3: Create vector store
vector_store = VectorStore(dimension=len(embeddings[0]))
vector_store.add(embeddings, all_chunks)

# Step 4: Ask a question
query = "What risks did management mention?"
query_embedding = embed_text([query])[0]

retrieved_chunks = vector_store.search(query_embedding, k=3)

# Step 5: Generate answer
answer = answer_question(query, retrieved_chunks)

print("\nQUESTION:")
print(query)

print("\nANSWER:")
print(answer)
