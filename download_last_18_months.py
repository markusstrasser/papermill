import os
import datetime
import arxiv
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def get_last_18_months_papers():
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=30*18)

    query = f'cat:cs.* AND submittedDate:[{start_date.year}{start_date.month:02d}{start_date.day:02d}0000 TO {end_date.year}{end_date.month:02d}{end_date.day:02d}2359]'

    search = arxiv.Search(query=query, max_results=2000, sort_by=arxiv.SortCriterion.SubmittedDate)
    results = list(search.results())
    return results

def download_paper_tar(paper, output_directory):
    tar_url = paper.pdf_url.replace("pdf", "src")
    tar_name = os.path.join(output_directory, f"{paper.title.replace('/', '-').replace(':', '-')}.tar")
    response = requests.get(tar_url)

    if response.status_code == 200:
        with open(tar_name, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {paper.title}")
    else:
        print(f"Failed to download: {paper.title}")

def parallel_download(paper, output_directory):
    try:
        download_paper_tar(paper, output_directory)
    except Exception as e:
        print(f"Error downloading {paper.title}: {e}")

def download_papers(output_directory, num_workers=10):
    papers = get_last_18_months_papers()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        tasks = [executor.submit(parallel_download, paper, output_directory) for paper in papers]
        for task in tqdm(tasks):
            task.result()

if __name__ == "__main__":
    output_directory = "data/tar_files"
    download_papers(output_directory)
