from LLM_Interface.construct_prompt import create_search_prompt, create_summarize_prompt, create_answer_prompt
from LLM_Interface.query_model import query_model
from helper.logging import Logging, Formatting
from Intent_classifier.intent_classifier import query_intent_classifier
import re
import click


log = Logging()
fmt = Formatting()
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS, no_args_is_help = True)
@click.option("-m", "--model", help="THe Ollama model you want to use.", required=True)




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


def check_model_is_pulled():
    pass

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
        elif intent == "summarize":
            prompt = create_summarize_prompt(user_input)
            print(query_model('llama2:7b',prompt))
        elif intent == "answer":
            prompt = create_answer_prompt(user_input)
            print(query_model('llama2:7b',prompt))
        # to do summarize and answer
    
if __name__ == "__main__":
    main()
    
