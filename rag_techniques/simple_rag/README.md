# Simple RAG
This project implements a lightweight Retrieval-Augmented Generation (RAG) pipeline designed for querying structured CSV data. It transforms csv data into vector embeddings, stores them in a FAISS vector index, and uses OpenAI's embedding model for semantic search. 

The goal is to build a lightweight system that can answer natural language questions about a CSV file.

The included dataset is a dummy customer information csv file that serves as the knowledge base for building a question-answering tool.

##  Key Components
- **Data Preprocessing**: Loads and parses CSV files using CSVLoader, followed by chunking with RecursiveCharacterTextSplitter.
- **Embedding & Indexing**: Generates vector embeddings using OpenAI’s embedding model and stores them in a FAISS vector store.
- **Vectorstore Management**: Supports persistent saving/loading of the vector store to avoid redundant computation.
- **Retrieval & Querying**: Retrieves relevant chunks based on user input and generates a natural language answer using a custom prompt.

## Use Cases
- Ask questions like `Who works at Acme Corp?` or `List all customers from Texas`.
- Build a semantic search interface over any structured CSV dataset.
- Serve as a foundation for more advanced enterprise RAG pipelines.