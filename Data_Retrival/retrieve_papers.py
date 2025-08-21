from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever

es_url = "https://05aa1e0d47ee450da2fc6a10f39fc911.us-central1.gcp.cloud.es.io:443"
es_api_key="SFJKWWhwZ0JxQjU3LVNLT1d4NmY6XzlHSXE2REV3MUM3eEhaQzQyUW80Zw=="

def extract_information(retrieved_docs):
    # flatten dictionary to get results
    retrieved_docs = retrieved_docs.body["hits"]["hits"]
    
    # creates a list of dicts with only the needed info
    document_list = []
    for doc in retrieved_docs:
        document_list.append(doc["_source"])
    print(document_list)
    return document_list
       

def retrive_papers(query):

    client = Elasticsearch(
        es_url,
        api_key=es_api_key
    )
    retrieved_docs = client.search(
    index="search-sep4",
    body={
        "_source": ["title", "abstract", "forenames", "keyname"],
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "abstract", "forenames", "keyname"]
            },
        },
    "min_score": 2.0
    }
    ) 
    retrieved_docs = extract_information(retrieved_docs)
    return retrieved_docs if retrieved_docs else None


