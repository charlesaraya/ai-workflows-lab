PROMPT_SYSTEM_GRADER = """You are a grader assessing relevance of a retrieved document to a user question.
If the document contains keyword(s) or semantic meaning related to the user question, grade it as relevant.
It does not need to be a stringent test. The goal is to filter out erroneous retrievals.
Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""

PROMPT_HUMAN_GRADER = "Retrieved document:\n{document}\n\nUser question:\n{question}"

PROMPT_SYSTEM_QA = """You are an assistant for question-answering tasks.
Answer the question based upon your knowledge.
Use three-to-five sentences maximum and keep the answer concise."""

PROMPT_HUMAN_QA = "Retrieved documents:\n\n<docs>{documents}</docs>\n\nUser question:<question>{question}</question>"