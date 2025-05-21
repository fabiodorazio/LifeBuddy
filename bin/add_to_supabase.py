import supabase
from supabase_connect import connect_to_supabase as cts

supabase = cts()

try:
    # Insert paper
    paper_data = {
        "paper_id": "PMID:123456",
        "title": "Fasting extends lifespan in mice",
        "doi": "10.1234/aging.2024",
        "source": "PubMed"
    }
    
    response = supabase.from_("ageing_papers").insert(paper_data).execute()  # Correct method

    # Check for errors
    if hasattr(response, 'error') and response.error:
        raise Exception(response.error)
    
    print("Insert successful:", response.data)
    
    
except Exception as e:
    print("Error:", str(e))