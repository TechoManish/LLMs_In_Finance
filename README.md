# LLMs_In_Finance
LLMs + Embeddings in Finance: From Search to Intelligence

With this project we intend to do the below 
A:ingestion of data - we would use a locally available dataset of 10k records
B:chunking
C:embeddings - FAISS
D:vector search (FAISS)
E:RAG-style Q&A module 

llm_finance_rag_demo/
│
├── data/
│   └── documents.py
│
├── embeddings/
│   └── embedder.py
│
├── retrieval/
│   └── vector_store.py
│
├── rag/
│   └── qa.py
│
├── utils/
│   └── chunking.py
│
├── main.py
├── requirements.txt

Libraries needed:
openai
faiss-cpu
numpy

└── README.md

