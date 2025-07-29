from sickle import Sickle
import requests
from PyPDF2 import PdfReader
from io import BytesIO
from elasticsearch import Elasticsearch, helpers

elastic_cloud_address = "https://my-elasticsearch-project-ee9962.es.us-west-2.aws.elastic.cloud:443",
index_name = "search-papers"

client = Elasticsearch(
    elastic_cloud_address,
    api_key="SUlhVUw1Z0J5X3JBUlFBZGR1ZjI6VlZ3R2pGaDRYMmxRYjNSLWF5S2FoUQ=="
)

def create_mappings():
    mappings = {
        "properties": {
            "id":        {"type": "keyword"},
            "created":   {"type": "date"},   # default: yyyy-MM-dd
            "updated":   {"type": "date"},
            "authors":   {"type": "list"},  # or "text" if full name search desired
            "author":    {"type": "list"},  # or "text"
            "keyname":   {"type": "keyword"},
            "forenames": {"type": "text"},
            "title":     {"type": "text"},
            "categories":{"type": "keyword"},
            "comments":  {"type": "text"},
            "report-no": {"type": "keyword"},
            "abstract":  {"type": "text"},
        }
    }
    mapping_response = client.indices.put_mapping(index=index_name, body=mappings)
    print(mapping_response)


def flatten_lists_in_dict(d, join_str="\n"):
    """
    Given a dictionary `d`, convert any value that is a list into a string by 
    joining the list elements with `join_str`.
    Returns a new dictionary with updated values.
    """
    new_dict = {}
    for k, v in d.items():
        if isinstance(v, list):
            # Convert list to string, joining elements
            # Optionally convert non-str elements to str before joining
            str_items = [str(item) for item in v]
            new_dict[k] = join_str.join(str_items)
        else:
            new_dict[k] = v
    return new_dict


sickle = Sickle('http://export.arxiv.org/oai2')
records = sickle.ListRecords(metadataPrefix='arXiv', set='cs')
i = 0
record_upload = []
for record in records:
    if i == 10:
        bulk_response = helpers.bulk(client, record_upload, index=index_name)
        print(bulk_response)
        break
    metadata = flatten_lists_in_dict(record.metadata)
    #pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    record_upload.append(metadata)
    i += 1
    
    
    