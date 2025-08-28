from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever

es_url = "https://0b2abe041d7d4a2184d65c7fd0c1e053.us-central1.gcp.cloud.es.io:443"
es_api_key="TC1icDhwZ0JLTDItN0EwbnI4UUk6MGc1a1lvMk9pWGpnYnRLdm12amlRUQ=="

# Initialize Elasticsearch client with your connection info
client = Elasticsearch(
    "https://0b2abe041d7d4a2184d65c7fd0c1e053.us-central1.gcp.cloud.es.io:443",
    api_key=es_api_key
)


def get_body_function(query):
    return {
        "_source": ["title", "abstract", "forenames", "keyname"],
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "abstract", "forenames", "keyname"]
            }
        },
        "min_score": 2.0
    } 

def retrive_papers(query):

    retriever = ElasticsearchRetriever(
        es_client=client,
        index_name="search-sep4",
        content_field="abstract",
        body_func=get_body_function
    )
    
    documents = retriever.invoke(query)
    papers = []
    for doc in documents:
        paper = {
            "abstract": doc.page_content,
            **doc.metadata  # unpacks metadata dict keys and values
        }
        papers.append(paper)

    return papers if papers else None

def main():
    retrive_papers("two-point")

if __name__ == "__main__":
    main()

