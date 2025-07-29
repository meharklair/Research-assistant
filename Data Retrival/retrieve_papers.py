from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever

elastic_cloud_address = "https://my-elasticsearch-project-ee9962.es.us-west-2.aws.elastic.cloud:443",
api_key = "U0xrWE5aZ0JQcFBpODk4akFvclU6WWFFVW80RUZjWDR4Tzd0T2VhZ1BRUQ=="


client = Elasticsearch(
    "https://my-elasticsearch-project-ee9962.es.us-west-2.aws.elastic.cloud:443",
    api_key="U0xrWE5aZ0JQcFBpODk4akFvclU6WWFFVW80RUZjWDR4Tzd0T2VhZ1BRUQ=="
)

retriever_object = {
    "standard": {
        "query": {
            "multi_match": {
                "query": "Artificial",
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
for item in search_response['hits']['hits']:
    print(item)
    