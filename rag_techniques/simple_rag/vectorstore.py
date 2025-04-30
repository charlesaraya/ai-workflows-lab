import os

import faiss
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_community.docstore.in_memory import InMemoryDocstore

def init_embedding(model):
    return OpenAIEmbeddings(model=model)

def build_vectorstore(chunks, embedding_model):
    print("Building new vectorstore...")
    embedding = init_embedding(embedding_model)
    index = faiss.IndexFlatL2(len(OpenAIEmbeddings().embed_query(" ")))
    vector_store = FAISS(
        embedding_function = embedding,
        index = index,
        docstore = InMemoryDocstore(),
        index_to_docstore_id = {}
    )
    return vector_store.from_documents(chunks, embedding)

def save_vectorstore(vs, path):
    vs.save_local(path)
    print(f"Vectorstore saved to {path}")

def load_vectorstore(path, embedding_model):
    if os.path.exists(path):
        try:
            print(f"Loading existing vectorstore from {path}")
            embedding = init_embedding(embedding_model)
            return FAISS.load_local(path, embeddings=embedding, allow_dangerous_deserialization=True)
        except Exception as e:
            print(f"Failed to load vectorstore: {e}")
            return None
