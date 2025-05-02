# main.py
from pipeline import run_pipeline
from config import load_config
from retriever import build_retrieval_grader_chain, build_qa_chain
from preprocessor import format_docs

from config import set_env

if __name__ == "__main__":
    config = load_config("config/config.yaml")
    set_env(config["llm_api_key_name"])
    set_env(config["embedding_api_key_name"])
    retriever = run_pipeline(config)

    retrieval_grader = build_retrieval_grader_chain(config["llm_model"], config["temperature"])
    qa_chain = build_qa_chain(config["llm_model"], config["temperature"])

    print("\nAsk me anything about __ (type 'exit' to quit)\n")
    while True:
        query = input(">> ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        try:
            docs = retriever.invoke(query)
            docs_to_use = []
            for doc in docs:
                print(doc.page_content, '\n', '-'*50)
                res = retrieval_grader.invoke({"question": query, "document": doc.page_content})
                print(res,'\n')
                if res.binary_score == 'yes':
                    docs_to_use.append(doc)
            generation = qa_chain.invoke({"documents":format_docs(docs_to_use), "question": query})
        except Exception as e:
            print(f"Error: {e}")