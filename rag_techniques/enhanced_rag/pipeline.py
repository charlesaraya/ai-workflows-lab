import os

from langchain.text_splitter import RecursiveCharacterTextSplitter

from preprocessor import preprocess_urls
from vectorstore import build_vectorstore, load_vectorstore

def run_pipeline(config):
    docs = preprocess_urls(config["input_file"])
    # Chunking
    splitter = RecursiveCharacterTextSplitter(chunk_size=config['chunk_size'], chunk_overlap=config['chunk_overlap'])
    chunks = splitter.split_documents(docs)

    # Build vectorstore
    embedding_model = config['embedding_model']
    db_path = config["db_path"]
    vectorstore = load_vectorstore(db_path, embedding_model)
    if not vectorstore:
        vectorstore = build_vectorstore(chunks, embedding_model, db_path)

    retriever = vectorstore.as_retriever(
                search_type="similarity",
                search_kwargs={'k': 4}, # number of documents to retrieve
            )
    return retriever
