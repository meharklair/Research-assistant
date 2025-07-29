from langchain.prompts import PromptTemplate
import retrieve_papers

user_query = "Can you find me a paper that has to do with decentralized growth for Artificial Neural Networks?"
# Example prompt template
prompt_template = """You are an AI assistant.
Given the following contexts, answer the user's question as accurately as possible.

CONTEXT:
{context}

QUESTION:
{question}

Answer:"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)
retrieved_docs = retrieve_papers.retrive_papers(user_query)
print(retrieved_docs)
# Concatenate or summarize retrieved passages
context = "\n\n".join(doc.page_content for doc in retrieved_docs)
formatted_prompt = prompt.format(context=context, question=user_query)
print(formatted_prompt)