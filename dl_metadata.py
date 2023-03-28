import requests
from datetime import datetime, timedelta
from lxml import etree
import time

def download_metadata(start_date, end_date):
    base_url = "https://export.arxiv.org/oai2"
    cs_papers = []

    while start_date < end_date:
        until_date = start_date + timedelta(days=30)
        if until_date > end_date:
            until_date = end_date

        params = {
            "verb": "ListRecords",
            "metadataPrefix": "arXiv",
            "set": "cs",
            "from": start_date.strftime("%Y-%m-%d"),
            "until": until_date.strftime("%Y-%m-%d")
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()

        xml = etree.fromstring(response.content)
        for record in xml.xpath("//oai:record", namespaces={"oai": "http://www.openarchives.org/OAI/2.0/"}):
            metadata = record.find("oai:metadata", namespaces={"oai": "http://www.openarchives.org/OAI/2.0/"})
            if metadata is not None:
                cs_papers.append(metadata.find("arXiv:arXiv", namespaces={"arXiv": "http://arxiv.org/OAI/arXiv/"}))

        start_date = until_date
        time.sleep(5)

    return cs_papers

if __name__ == "__main__":
    start_date = datetime(2021, 8, 1)
    end_date = datetime.now()

    cs_papers = download_metadata(start_date, end_date)
    root = etree.Element("metadata")
    for paper in cs_papers:
        root.append(paper)

    with open("cs_metadata.xml", "wb") as f:
        f.write(etree.tostring(root, pretty_print=True))
