from langchain.prompts import PromptTemplate
from Data_Retrival.retrieve_papers import retrive_papers

def create_prompt(user_query):
    # Example prompt template
    user_prompt = """
    AUTOMATICALLY RETRIEVED CONTEXT:
    {context}
    """ 
    system_prompt = """
    You are an expert researcher in the Computer Science domain. You will act as a research assistant who displays research papers, based on the retreived content display the names of each paper and give a brief explanation.\n
    If the retrieved context is None only say I was unable to find papers on the topic. MAKE SURE TO ONLY USE THE RETRIEVED CONTENT. THE USER IS NOT PROVIDING THE RETRIEVED CONTEXT.
    """


    prompt = PromptTemplate(
        template=user_prompt,
        input_variables=["context"]
    )
    
    context = retrive_papers(user_query)

    # Concatenate or summarize retrieved passages
    if context != None:
        context = "\n\n".join(doc.page_content for doc in context)
        
    user_prompt = prompt.format(context=context)
    messages =[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ]

    return messages