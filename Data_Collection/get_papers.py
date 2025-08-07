from sickle import Sickle
import requests
from PyPDF2 import PdfReader
from io import BytesIO
from elasticsearch import Elasticsearch, helpers

elastic_cloud_address = "https://05aa1e0d47ee450da2fc6a10f39fc911.us-central1.gcp.cloud.es.io:443"
index_name = "search-sep4"

client = Elasticsearch(
    elastic_cloud_address,
    api_key="SFJKWWhwZ0JxQjU3LVNLT1d4NmY6XzlHSXE2REV3MUM3eEhaQzQyUW80Zw=="
)

def create_mappings():
    mappings = {
        "properties": {
            "id":        {"type": "keyword"},
            "created":   {"type": "date"},   # default: yyyy-MM-dd
            "updated":   {"type": "date"},
            "keyname":   {"type": "keyword"},
            "forenames": {"type": "text"},
            "title":     {"type": "text"},
            "comments":  {"type": "text"},
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

#create_mappings()
sickle = Sickle('http://export.arxiv.org/oai2')
records = sickle.ListRecords(metadataPrefix='arXiv', set='cs')
i = 0
record_upload = []
for record in records:
    if i == 5:
        bulk_response = helpers.bulk(client, record_upload, index=index_name)
        print(bulk_response)
        break
    metadata = flatten_lists_in_dict(record.metadata)
    #pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    record_upload.append(metadata)
    i += 1
    
    
    