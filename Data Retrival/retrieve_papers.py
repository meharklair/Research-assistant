from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever


client = Elasticsearch(
    "https://my-elasticsearch-project-ee9962.es.us-west-2.aws.elastic.cloud:443",
    api_key="U0xrWE5aZ0JQcFBpODk4akFvclU6WWFFVW80RUZjWDR4Tzd0T2VhZ1BRUQ=="
)

def retrieve_data(query):
    retriever_object = {
        "standard": {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": [
                        "title"
                    ]
                }
            }
        }
    }

    search_response = client.search(
        index="search-papers",
        retriever=retriever_object,
    )
    return search_response['hits']['hits']

        
retrieve_data("artificial")