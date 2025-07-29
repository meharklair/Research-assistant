from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever

es_url = "https://my-elasticsearch-project-ee9962.es.us-west-2.aws.elastic.cloud:443"
es_api_key="U0xrWE5aZ0JQcFBpODk4akFvclU6WWFFVW80RUZjWDR4Tzd0T2VhZ1BRUQ=="


client = Elasticsearch(
    "https://my-elasticsearch-project-ee9962.es.us-west-2.aws.elastic.cloud:443",
    api_key="U0xrWE5aZ0JQcFBpODk4akFvclU6WWFFVW80RUZjWDR4Tzd0T2VhZ1BRUQ=="
)

def retrive_papers(query):
    def bm25_query(search_query: str) -> dict:
        return {
            "query": {
                "match": {
                    text_field: search_query,
                },
            },
        }

    text_field = "abstract"
    retriever = ElasticsearchRetriever.from_es_params(
        index_name="search-papers",
        body_func=bm25_query,
        content_field=text_field,
        url=es_url,
        api_key=es_api_key
    )
    
    return retriever.invoke(query)