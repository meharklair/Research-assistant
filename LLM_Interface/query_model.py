import ollama

def query_model(model, messages):
    if messages == None:
        return "Sorry, I was unable to find any papers"
    response = ollama.chat(
        model=model,
        messages=messages
    )
    
    return response['message']['content']