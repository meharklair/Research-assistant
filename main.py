from fastapi import FastAPI
from LLM_Interface.construct_prompt import create_search_prompt
from LLM_Interface.query_model import query_model

import re
app = FastAPI()


def normalize_query(user_query):
    ''' normalizes the search query
        I might need to change this to an LLM extractor or using intent
    
    '''
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
    prompt = create_search_prompt(normalized_query)
    return query_model('llama2:7b', prompt)

def main():
    print_ascii()
    exit()
    while True:
        user_input = input("What would you like to ask?")
        prompt = create_search_prompt(user_input)
        print(query_model('llama2:7b',prompt))
    


@staticmethod
def print_ascii():
    ascii_art = """
                                                                                   
                                                                                            

    """
    print(ascii_art)
    
if __name__ == "__main__":
    main()
    
