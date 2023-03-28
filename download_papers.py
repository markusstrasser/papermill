import os
import requests
from lxml import etree
from tqdm import tqdm
from datetime import datetime, timedelta

def download_pdf(url, output_folder):
    response = requests.get(url)
    response.raise_for_status()

    filename = url.split("/")[-1]
    output_path = os.path.join(output_folder, filename)

    with open(output_path, "wb") as f:
        f.write(response.content)

def get_papers_from_last_18_months(metadata_file):
    tree = etree.parse(metadata_file)
    root = tree.getroot()

    end_date = datetime.now()
    start_date = end_date - timedelta(days=18*30)

    papers = []

    for paper in root.findall('.//{http://arxiv.org/OAI/arXiv/}arXiv'):
        date_element = paper.find('{http://arxiv.org/OAI/arXiv/}created')
        if date_element is not None:
            date = datetime.strptime(date_element.text, "%Y-%m-%d")
            if start_date <= date <= end_date:
                papers.append(paper)

    return papers

if __name__ == "__main__":
    metadata_file = "cs_metadata.xml"
    output_folder = "data/pdfs"

    os.makedirs(output_folder, exist_ok=True)

    papers = get_papers_from_last_18_months(metadata_file)
    pdf_base_url = "https://export.arxiv.org/pdf/"
    
    print(f"Found {len(papers)} papers to download")

    for paper in tqdm(papers, desc="Downloading PDFs"):
        identifier = paper.find('{http://arxiv.org/OAI/arXiv/}id').text
        pdf_url = f"{pdf_base_url}{identifier}"
        download_pdf(pdf_url, output_folder)
