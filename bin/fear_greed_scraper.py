import requests
from bs4 import BeautifulSoup
import pandas as pd

# Load the archived HTML (replace with your local file or URL)
url = "https://web.archive.org/web/20131212152525/http://money.cnn.com/data/fear-and-greed/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the 7 indicators
indicators = []
panels = soup.find_all("div", class_="panel")  # Each indicator is in a "panel" div

for panel in panels:
    label = panel.find("div", class_="label").get_text(strip=True)
    rating = panel.find("div", class_="wsod_fRight").get_text(strip=True)
    description = panel.find("div", class_="smarttext").get_text(strip=True)
    
    indicators.append({
        "Indicator": label.replace("▼", "").replace("▲", "").strip(),
        "Rating": rating,
        "Description": description
    })

# Convert to DataFrame
df = pd.DataFrame(indicators)
print(df)

# Save to CSV
df.to_csv("fear_greed_indicators_2013.csv", index=False)