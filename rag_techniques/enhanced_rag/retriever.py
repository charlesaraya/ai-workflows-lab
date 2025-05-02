from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from pydantic import BaseModel, Field

from prompt import (
    PROMPT_SYSTEM_GRADER,
    PROMPT_HUMAN_GRADER,
    PROMPT_SYSTEM_QA,
    PROMPT_HUMAN_QA
)

def build_retrieval_chain(vectorstore=None, llm=None, prompt=None, search_type=None, top_k=None):
    if vectorstore:
        retriever = vectorstore.as_retriever(
            search_type = search_type,
            search_kwargs = {"k": top_k}
        )
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        return create_retrieval_chain(retriever, question_answer_chain)


# Data model
class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""
    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )

def build_retrieval_grader_chain(model, temperature):
    grader_prompt = ChatPromptTemplate.from_messages([
            ("system", PROMPT_SYSTEM_GRADER),
            ("human", PROMPT_HUMAN_GRADER),
        ])
    llm = ChatGroq(model=model, temperature=temperature)
    structured_llm_grader = llm.with_structured_output(GradeDocuments)
    retrieval_grader = grader_prompt | structured_llm_grader
    return retrieval_grader

def build_qa_chain(model, temperature):
    # QA Prompt
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", PROMPT_SYSTEM_QA),
        ("human", PROMPT_HUMAN_QA),
    ])
    llm = ChatGroq(model=model, temperature=temperature)
    rag_chain = qa_prompt | llm | StrOutputParser()
    return rag_chain