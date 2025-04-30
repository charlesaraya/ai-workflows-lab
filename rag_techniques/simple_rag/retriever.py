#from langchain.chains import RetrievalQA
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

def retrieve_context(query, config):
    # Example: FAISS or Chroma + optional reranking
    return ["Relevant doc 1", "Relevant doc 2"]

def build_retrieval_chain(vectorstore, llm, prompt, top_k):
    retriever = vectorstore.as_retriever(search_kwargs={"k": top_k})
    #return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    # Create the question-answer chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)


