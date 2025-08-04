from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
import retrieve_papers
import ollama


user_query = "Can you find me a paper that has to do with decentralized growth for Artificial Neural Networks?"
# Example prompt template
user_prompt = """
Given the following contexts, answer the user's question as accurately as possible.

CONTEXT:
{context}

QUESTION:
{question}

Answer:
"""
system_prompt = """
You are an expert researcher in the Computer Science domain. You will act as a research assistant answering question and finding papers based on the users questions.
"""


prompt = PromptTemplate(
    template=user_prompt,
    input_variables=["context", "question"]
)
retrieved_docs = retrieve_papers.retrive_papers(user_query)
#print(retrieved_docs)
# Concatenate or summarize retrieved passages
context = "\n\n".join(doc.page_content for doc in retrieved_docs)
user_prompt = prompt.format(context=context, question=user_query)

response = ollama.chat(
    model='llama2',
    messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt},
    ]
)
print(response['message']['content'])