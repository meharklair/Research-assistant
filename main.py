from LLM_Interface.construct_prompt import create_prompt
from fastapi import FastAPI
from LLM_Interface.construct_prompt import create_prompt
from LLM_Interface.query_model import query_model

import re
app = FastAPI()

def normalize_query(user_query):
    phrases_to_remove = [
        r"can you find me", r"please find", r"show me", r"look up", r"find papers on"
    ]
    normalized = user_query.lower()
    for phrase in phrases_to_remove:
        normalized = re.sub(phrase, "", normalized)
    return normalized.strip()

@app.get("/search")
async def search_papers(query):
    # Search for papers with matching title in your Elasticsearch index (e.g., "papers")
    normalized_query = normalize_query(query)
    prompt = create_prompt(normalized_query)
    return query_model('tinyllama:1.1b', prompt)

def main():
    prompt = create_prompt("Neural Networks in an Artificial Chemistry")
    print(prompt)
    print(query_model('tinyllama:1.1b',prompt))
    
    
    
    
if __name__ == "__main__":
    main()
    
