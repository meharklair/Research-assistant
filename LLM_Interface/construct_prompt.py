from langchain.prompts import PromptTemplate
from Data_Retrival.retrieve_papers import retrive_papers

def create_search_prompt(user_query):
    # Example prompt template
    user_prompt = """
    For the explanation put a focus on how it relates to {user_query}
    AUTOMATICALLY RETRIEVED CONTEXT:\n
    {context}
    """ 
    system_prompt = """
    You are an expert researcher in the Computer Science domain. You will be provided with a paper/papers and your job is to list the paper and provide the name, the authors names, and a brief explanation.\n
    Begin each output with: "Here are what papers I found!"
    """


    prompt = PromptTemplate(
        template=user_prompt,
        input_variables=["context", "user_query"]
    )
    
    context = retrive_papers(user_query)
    if context == None:
        return None
    # Concatenate or summarize retrieved passages
  
    #context = "\n\n".join(doc.page_content for doc in context)
        
    user_prompt = prompt.format(context=context, user_query=user_query)
    messages =[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt},
        ]

    return messages