from LLM_Interface.construct_prompt import create_search_prompt, create_summarize_prompt, create_answer_prompt
from LLM_Interface.query_model import query_model
from helper.logging import Logging, Formatting
from Intent_classifier.intent_classifier import query_intent_classifier
from rake_nltk import Rake
import click

def remove_common_keywords(keywords):
    common_keywords = ["summarize","papers", "find", "paper", "find papers", "find a paper"]
    new_keywords = []
    for item in keywords:
        if item in common_keywords:
            continue
        else:
            new_keywords.append(item)
    return new_keywords

log = Logging()
fmt = Formatting()
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS, no_args_is_help = True)
@click.option("-m", "--model", help="The Ollama model you want to use (make sure you pull the model first).", required=True)

def main(model):
    fmt.print_ascii()
    fmt.print_help()


    while True:
        user_input = input("Enter your query below: \n")
        r = Rake()
        r.extract_keywords_from_text(user_input)
        keywords = r.get_ranked_phrases()
        print(keywords)
        keywords = remove_common_keywords(keywords)
        print(keywords)
        if user_input.lower() == "help":
            fmt.print_help()
            continue
        if user_input.lower() == "exit":
            print("shutting down beep boop...")
            exit()
        intent = query_intent_classifier(user_input)
        if intent == "search":
            prompt = create_search_prompt(keywords[-1])
            print(query_model(model,prompt))
        elif intent == "summarize":
            prompt = create_summarize_prompt(keywords[-1])
            print(query_model(model,prompt))
        elif intent == "answer":
            prompt = create_answer_prompt(keywords[-1])
            print(query_model(model,prompt))
        else:
            print("I did not understand your intent, sorry!\n please reword it and try again")
    
if __name__ == "__main__":
    main()
    
