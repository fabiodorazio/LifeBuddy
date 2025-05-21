from pubmed import fetch_pubmed_abstracts
from extract import extract_study_info
from db import save_to_db

def process_intervention(term: str):
    papers = fetch_pubmed_abstracts(term)
    for paper in papers:
        data = extract_study_info(paper)
        if data:
            save_to_db(data)

if __name__ == "__main__":
    process_intervention("Rapamycin aging")
