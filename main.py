from LLM_Interface.construct_prompt import create_search_prompt
from LLM_Interface.query_model import query_model
from helper.logging import Logging, Formatting
from Intent_classifier.intent_classifier import query_intent_classifier
import re


log = Logging()
fmt = Formatting()


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


def main():
    fmt.print_ascii()
    fmt.print_help()
    while True:
        user_input = input("Enter your query below: \n")
        if user_input.lower() == "help":
            fmt.print_help()
            continue
        if user_input.lower() == "exit":
            print("shutting down beep boop...")
            exit()
        intent = query_intent_classifier(user_input)
        if intent == "search":
            prompt = create_search_prompt(user_input)
            print(query_model('llama2:7b',prompt))
        # to do summarize and answer
    
if __name__ == "__main__":
    main()
    
