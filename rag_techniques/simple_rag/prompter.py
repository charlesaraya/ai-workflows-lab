import os

from langchain_core.prompts import ChatPromptTemplate

def build_prompt(path):
    base_path = os.path.dirname(__file__)
    prompt_path = os.path.join(base_path, path)
    with open(prompt_path, "r") as f:
        prompt = f.read()

    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt),
        ("human", "{input}"),
    ])
    return prompt
