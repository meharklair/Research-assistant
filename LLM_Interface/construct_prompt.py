from langchain.prompts import PromptTemplate
from Data_Retrival.retrieve_papers import retrive_papers

def create_search_prompt(user_query):
    # Example prompt template
    user_prompt = """
    You are summarizing the following papers in relation to the user's query:
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
    - **Explanation**: Brief summary highlighting how it relates to the user's query.

    Output Format:
    Begin with: "Here are what papers I found!:"
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



def create_answer_prompt(user_query):
    # Example prompt template
    user_prompt = """
    Using the automatically retrieved context below, answer the user's query as clearly and concisely as possible.

    AUTOMATICALLY RETRIEVED CONTEXT:
    {context}

    USER QUERY:
    {user_query} 
    """ 
    system_prompt = """
    You are an expert researcher specializing in Computer Science.
    Your task is to answer the user's query based on the provided context.

    GUIDELINES:
    1. Read the context thoroughly before answering.
    2. If context directly addresses the user's question, summarize and synthesize the information in your own words.
    3. If the context does not fully answer the query, explain what is missing, and provide the best possible answer based on available data.
    4. Focus your explanation on how the context relates to the user's question.
    5. Do not invent information not present in the context.
    6. Structure your answer using headings, bullet points, or tables if relevant for readability.
    7. Maintain a professional and scholarly tone throughout.
    8. If any part of the query cannot be answered from context, clearly point this out.

    OUTPUT FORMAT:
    - Begin with: "Here is the answer to your query:"
    - Follow with your structured, well-explained response.
    
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




def create_summarize_prompt(user_query):
    # Example prompt template
    user_prompt = """
    Using the automatically retrieved context below, Summarize each paper following the instructions below.

    AUTOMATICALLY RETRIEVED CONTEXT:
    {context}

    Instructions:
    1. Read the context thoroughly before summarizing.
    2. Break the paper up into sections (e.g., Introduction, Related work, Experiments, etc.). 
    3. Explain the paper section by section.
    """ 
    system_prompt = """
    You are an expert researcher specializing in Computer Science.
    Your task is to create a clear, concise, and well-structured summary based on the content provided. 

    GUIDELINES:
    1.Focus on main objectives, methods, results, and conclusions. 
    2. Do not add or assume information not present in the input text. 
    3. Maintain a scholarly and neutral tone. 
    4. Format the summary with clear paragraphs or bullet points. 

    OUTPUT FORMAT:
    - Begin with: "Here is your summary!:"
    - Follow with your structured, clear, and concise summary.    
    """


    prompt = PromptTemplate(
        template=user_prompt,
        input_variables=["context"]
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
