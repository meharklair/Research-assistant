from langchain.prompts import PromptTemplate
from Data_Retrival.retrieve_papers import retrive_papers

def create_search_prompt(user_query):
    # Example prompt template
    user_prompt = """
    You are summarizing the following papers in relation to the user’s query:
    User Query: {user_query}
    
    AUTOMATICALLY RETRIEVED CONTEXT:
    {context}

    Instructions:
    1. Extract each paper's title, abstract, and author list (if available).
    2. Provide a 2-3 sentence explanation of the paper.
    3. Explicitly connect the explanation back to the user query: "{user_query}".
    4. If details are missing (e.g., no authors provided), state that clearly instead of guessing.
    """ 
    system_prompt = """
    You are an expert researcher in the Computer Science domain. 
    You must analyze the provided context and create a structured list of relevant papers. 
    Each paper entry should include:
    - **Paper Title**
    - **Authors** (or state "Not available")
    - **Explanation**: Brief summary highlighting how it relates to the user’s query.

    Output Format:
    Begin with: "Here are what papers I found!"
    Then list each paper clearly using bullet points.
    Do not invent information not present in the context.
    Keep tone professional and concise.
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


