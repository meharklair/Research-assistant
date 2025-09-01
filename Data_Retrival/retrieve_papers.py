from elasticsearch import Elasticsearch, helpers
from langchain_elasticsearch import ElasticsearchRetriever
from sentence_transformers import SentenceTransformer
es_url = "https://0b2abe041d7d4a2184d65c7fd0c1e053.us-central1.gcp.cloud.es.io:443"
es_api_key="T19FTEE1a0JRai1JTFgtbDlNOWg6eFIyaXg4S1dUR19RYnF4ZGdPRnhDUQ=="

# Initialize Elasticsearch client with your connection info
client = Elasticsearch(
    "https://0b2abe041d7d4a2184d65c7fd0c1e053.us-central1.gcp.cloud.es.io:443",
    api_key=es_api_key
)


def get_body_function(query):

    query_embedding = generate_embeddings(query)

    return {
        "_source": ["title", "abstract", "forenames", "keyname"],
        "size": 3,
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": query,
                            "fields": ["title", "abstract", "forenames", "keyname"]
                        }
                    }
                ],
                "should": [
                    {
                        "script_score": {
                            "query": {"match_all": {}},
                            "script": {
                                "source": "cosineSimilarity(params.query_vector, 'vector') + 1.0",
                                "params": {"query_vector": query_embedding.tolist()}
                            }
                        }
                    }
                ]
            }
        }
    } 


def generate_embeddings(abstract):
    # Load the embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(abstract, convert_to_tensor=False)
    
    return embeddings

def retrive_papers(query):

    retriever = ElasticsearchRetriever(
        es_client=client,
        index_name="search-8p5q",
        content_field="abstract",
        body_func=get_body_function
    )
    documents = retriever.invoke(query)
    print(documents)
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

