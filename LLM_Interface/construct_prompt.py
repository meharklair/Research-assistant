from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from Data_Retrival.retrieve_papers import retrive_papers
import ollama

def create_prompt(user_query):
    # Example prompt template
    user_prompt = """
    Using only the following retrieved documents, answer the user’s question as accurately as possible. If the answer is not contained in these documents, say "I don't know."

    AUTOMATICALLY RETRIEVED CONTEXT:
    {context}

    QUESTION:
    {question}

    Answer:
    """
    system_prompt = """
    You are an expert researcher in the Computer Science domain. MAKE SURE TO ONLY USE THE RETRIEVED CONTENT. You will act as a research assistant, answering questions and finding papers based on information automatically retrieved from relevant documents. THE CONTEXT IS NOT PROVIDED BY THE USER.
    """


    prompt = PromptTemplate(
        template=user_prompt,
        input_variables=["context", "question"]
    )
    retrieved_docs = retrive_papers(user_query)
    #print(retrieved_docs)
    # Concatenate or summarize retrieved passages
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)
    user_prompt = prompt.format(context=context, question=user_query)

    response = ollama.chat(
        model='llama2:7b',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ]
    )

    return response['message']['content']