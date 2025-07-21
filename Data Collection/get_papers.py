from sickle import Sickle
import requests
from PyPDF2 import PdfReader
from io import BytesIO

sickle = Sickle('http://export.arxiv.org/oai2')
records = sickle.ListRecords(metadataPrefix='arXiv', set='cs')

for record in records:
    metadata = record.metadata
    arxiv_id = metadata["id"][0]
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    print(metadata)
    print(arxiv_id)
    # Step 1: Stream PDF
    response = requests.get(pdf_url, stream=True)
    pdf_content = BytesIO(response.content)

    # Step 2: Extract Text In-Memory
    reader = PdfReader(pdf_content)
    full_text = "".join(page.extract_text() for page in reader.pages)
    print(full_text)
    exit()