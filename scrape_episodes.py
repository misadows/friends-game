import requests
from bs4 import BeautifulSoup
import json

url = 'https://pl.wikipedia.org/wiki/Lista_odcinków_serialu_Przyjaciele'  
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.findAll('table', {"class": "wikitable"})

results = []
for i, table in enumerate(tables[1:-2]):
    rows = table.findAll('tr')
    for row in rows:
        cells = row.findAll('td')
        if cells and len(cells)>=2:
            title = cells[2].get_text(strip=True)
            title_english = cells[1].get_text(strip=True)
            results.append({"title": title, "title_english": title_english, "season": i+1})
with open('friends-episodes.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
