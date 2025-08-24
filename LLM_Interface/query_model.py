from ollama import chat

def query_model(model, messages):
    if messages == None:
        return "Sorry, I was unable to find any papers"
    response = chat(
        model=model,
        messages=messages
    )
    
    return response['message']['content']