from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever

es_url = "https://05aa1e0d47ee450da2fc6a10f39fc911.us-central1.gcp.cloud.es.io:443"
es_api_key="SFJKWWhwZ0JxQjU3LVNLT1d4NmY6XzlHSXE2REV3MUM3eEhaQzQyUW80Zw=="



def retrive_papers(query):

    client = Elasticsearch(
        es_url,
        api_key=es_api_key
    )
    retrived_docs = client.search(
    index="search-sep4",
    body={
        "_source": ["title", "abstract", "keywords", "content"],
        "query": {
            "multi_match": {
                "query": "neural networks image recognition",
                "fields": ["title", "abstract", "forenames", "keyname"]
            },
        },
    "min_score": 2.0
    }
    ) 
    # flatten dictionary to get results
    retrived_docs = retrived_docs.body["hits"]["hits"]

    # extracts the dictionary in the list
    merged_dict = {}
    for d in retrived_docs:
        merged_dict.update(d)
    retrived_docs = merged_dict["_source"]
    print(retrived_docs)
    return retrived_docs if retrived_docs else None