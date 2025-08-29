# AI Research Assistant
## Overview
This project is a scalable research tool built on Elasticsearch, enhanced with semantic vector search and keyword matching. It is designed to support advanced retrieval functionalities such as hybrid search, filtering, and summarization with LLMs.

## Key Features
#### Keyword and Semantic Search 
Combines traditional Elasticsearch full-text keyword search with dense vector embeddings for contextual similarity.

#### Modular Query System
Supports multiple query intents such as search, summarization, and question answering integrated with LLMs.

#### Customizable Prompts
Uses prompt templates to leverage large language models (LLMs) for enhanced query understanding and response generation.

#### Extendable Indexing
Easily index papers with metadata fields and vector embeddings for semantic retrieval.


## Getting started 

> [!important]
> You need to create your own elasticsearch database with papers for this to work. I really wanted to have that included but elasticsearch is so crazy expensive.

### Installation
```bash
git clone https://github.com/meharklair/Research-assistant.git
cd Research-assistant
pip install -r requirements.txt
```
### Ollama set up 
first download ollama and then pull the model you want. Check the memory the model uses and choose the best one for your machine.
```bash
ollama pull llama2:7b
```
>[!note]
> Ollama will run the model locally on your computer.

### Elasticsearch Setup
I already have the code to create the mappings and ingest the papers in get_papers.py.
You just need to input your api key, index name, and elasticsearch URL.
```bash
elastic_cloud_address = YOUR_ADDRESS_HERE
index_name = INDEX_NAME_HERE
es_api_key = YOUR_API_KEY_HERE
```
### Running the Application
Run the main.py file and you should be presented with a help menu that will guide you.
```bash
python main.py --model your-llm-model-name
```
### Usage
You can enter queries for searching, summarizing, or answering, it will automatically decide what you are doing using an intent classifier.
Search: Find relevant papers by keywords or concepts.

Summarize: Generate concise summaries of papers.

Answer: Get direct answers sourced from indexed content.
> [!important]
> Since the LLM is running locally and the prompts are fairly complex your query may take a minute or two to run.
