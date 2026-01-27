# LLMs_In_Finance
LLMs + Embeddings in Finance: From Search to Intelligence

Financial insights are often buried in unstructured text like customer interactions, research notes, news, macro commentary, emails, chat logs etc making it slow and manual to extract meaning using traditional search.
By leveraging AI techniques such as Embeddings we can turn financial text into searchable semantic vectors.
We can then use the vector database to retrieves relevant context, and then leverage LLM to uses that context to generate intelligence by accelerating analysis while still keeping results auditable and reliable.

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

Here is a description of files used in this program
documents.py → “This simulates earnings calls / filings”
chunking.py → “This controls context quality”
embedder.py → “This is how text becomes searchable”
vector_store.py → “This replaces keyword search”
qa.py → “This is where reasoning happens”
main.py → “This is the full RAG pipeline”

To run the program 
bash
python main.py


└── README.md

