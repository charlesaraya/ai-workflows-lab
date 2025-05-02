import os

from langchain_community.document_loaders import WebBaseLoader

def preprocess_urls(path):
    urls = []
    with open(path) as infile:
        for line in infile:
            urls.append(line)
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]
    return docs_list

def format_docs(docs):
    return "\n".join(f"<doc{i+1}>:\nTitle:{doc.metadata['title']}\nSource:{doc.metadata['source']}\nContent:{doc.page_content}\n</doc{i+1}>\n" for i, doc in enumerate(docs))

