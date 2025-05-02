import os

from langchain_cohere import CohereEmbeddings
from langchain_chroma import Chroma

def init_embedding(model_name):
    return CohereEmbeddings(model=model_name)

def build_vectorstore(chunks, embedding_model_name, path):
    print("Building new vectorstore...")
    embedding_model = init_embedding(embedding_model_name)
    return Chroma.from_documents(
        documents = chunks,
        collection_name = "rag",
        embedding = embedding_model,
        persist_directory = path, 
    )

def load_vectorstore(path, embedding_model):
    if os.path.exists(path):
        try:
            print(f"Loading existing vectorstore from {path}")
            embedding = init_embedding(embedding_model)
            return Chroma(
                collection_name="rag",
                embedding_function=embedding,
                persist_directory=path,
            )
        except Exception as e:
            print(f"Failed to load vectorstore: {e}")
            return None
