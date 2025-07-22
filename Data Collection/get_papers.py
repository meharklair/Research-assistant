from sickle import Sickle
import requests
from PyPDF2 import PdfReader
from io import BytesIO
from elasticsearch import Elasticsearch, helpers

elastic_cloud_address = "id",
 

client = Elasticsearch(
    elastic_cloud_address,
    api_key="KEY"
)
index_name = "search-papers"


mappings = {
    "properties": {
        "id":        {"type": "keyword"},
        "created":   {"type": "date"},   # default: yyyy-MM-dd
        "updated":   {"type": "date"},
        "authors":   {"type": "text"},  # or "text" if full name search desired
        "author":    {"type": "text"},  # or "text"
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

sickle = Sickle('http://export.arxiv.org/oai2')
records = sickle.ListRecords(metadataPrefix='arXiv', set='cs')

record_upload = []
i = 0
for record in records:
    if i == 3:
        break
    metadata = record.metadata
    arxiv_id = metadata["id"][0]
    #pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    record_upload.append(metadata)
    i += 1
    
    bulk_response = helpers.bulk(client, record_upload, index=index_name)
    print(bulk_response)
    
    
  