from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever

es_url = "https://05aa1e0d47ee450da2fc6a10f39fc911.us-central1.gcp.cloud.es.io:443"
es_api_key="SFJKWWhwZ0JxQjU3LVNLT1d4NmY6XzlHSXE2REV3MUM3eEhaQzQyUW80Zw=="



def retrive_papers(query):
    def bm25_query(search_query: str) -> dict:
        return {
            "query": {
                "multi_match": {
                    "query": search_query,
                    "fields": [
                        "abstract",
                        "fornames",
                        "keyname",
                        "title"
                    ]
                },
            },
        "min_score": 2.0  
        }

    text_field = "abstract"
    retriever = ElasticsearchRetriever.from_es_params(
        index_name="search-sep4",
        body_func=bm25_query,
        content_field=text_field,
        url=es_url,
        api_key=es_api_key
    )
    retrived_docs = retriever.invoke(query)
    return retrived_docs if retrived_docs else None