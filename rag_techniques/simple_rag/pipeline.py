import os

from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

from preprocessor import preprocess_csv
from retriever import build_retrieval_chain
from prompter import build_prompt
from vectorstore import build_vectorstore, save_vectorstore, load_vectorstore
from config import set_env

def run_pipeline(config):
    set_env(config["api_key_name"])

    docs = preprocess_csv(config["input_file"])

    # Chunking
    splitter = RecursiveCharacterTextSplitter(chunk_size=config['chunk_size'], chunk_overlap=config['chunk_overlap'])
    chunks = splitter.split_documents(docs)

    # Load, or Build and Save vectorstore
    db_path = config['vectorstore_path']
    embedding_model = config['embedding_model']
    vectorstore = load_vectorstore(db_path, embedding_model)
    if not vectorstore:
        vectorstore = build_vectorstore(chunks, embedding_model)
        save_vectorstore(vectorstore, db_path)

    # Create prompt
    prompt = build_prompt(config["prompt_template"])

    # Create retrieval chain
    llm = ChatOpenAI(temperature=config["temperature"], model=config["llm_model"])
    rag_chain = build_retrieval_chain(vectorstore, llm, prompt, config['top_k'])

    return rag_chain
