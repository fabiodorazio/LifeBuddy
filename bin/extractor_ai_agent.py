import requests

DEEPSEEK_API_KEY = "your-api-key"
headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}

def ask_deepseek(prompt):
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        json=data,
        headers=headers
    )
    return response.json()["choices"][0]["message"]["content"]


'''
import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def extract_study_info(paper):
    prompt = f"""
You are an expert biomedical data extraction agent. Given the abstract below, extract structured information as JSON:

Abstract:
\"\"\"
{paper['abstract']}
\"\"\"

Return fields: intervention, species, effect, direction (positive/negative/neutral), outcome_type, metric (if available), evidence_strength, study_type, publication_year (if known), study_link.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Extract structured scientific evidence."},
                  {"role": "user", "content": prompt}],
        temperature=0.2,
    )

    try:
        result = response.choices[0].message.content
        return eval(result)  # Or use json.loads if well-formed
    except Exception as e:
        print("Parsing failed:", e)
        return None

'''