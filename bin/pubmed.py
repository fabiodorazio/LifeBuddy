from Bio import Entrez

Entrez.email = "you@example.com"

def fetch_pubmed_abstracts(query: str, max_results=10):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    ids = record["IdList"]

    results = []
    for pmid in ids:
        fetch = Entrez.efetch(db="pubmed", id=pmid, rettype="abstract", retmode="text")
        abstract = fetch.read()
        results.append({
            "pmid": pmid,
            "abstract": abstract,
            "link": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"
        })
    return results
