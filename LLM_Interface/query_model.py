import ollama

def query_model(model, messages):
    response = ollama.chat(
        model=model,
        messages=messages
    )
    
    return response['message']['content']    