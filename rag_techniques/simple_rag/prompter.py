import os

from langchain_core.prompts import ChatPromptTemplate

def build_prompt(path):
    with open(path, "r") as f:
        prompt = f.read()

    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt),
        ("human", "{input}"),
    ])
    return prompt
