import requests
from bs4 import BeautifulSoup

print("Collez votre liste (terminez avec CTRL+D sur macOS/Linux ou CTRL+Z puis Entrée sur Windows):")

# Read multiline input
import sys
lines = sys.stdin.read().strip().splitlines()
chunks = [lines[i:i+3] for i in range(0, len(lines), 3)]

for chunk in chunks:
    if len(chunk) != 3:
        print(f"⚠️ Entrée incomplète ignorée: {chunk}")
        continue

    page_id, page_name, url = chunk
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for title tag in head
        head_tag = soup.find('head')
        title_tag = soup.find('title')
        
        title_exists = title_tag is not None
        title_text = title_tag.text.strip() if title_tag else "Non trouvé"
        
        print(f"{page_id} | {page_name} | {url}")
        print(f"{page_id} | 8.5 - title : {'✅ ' + title_text if title_exists else '❌ Non trouvé'}")
        print("--------------------------------")
    except Exception as e:
        print(f"{page_id} | {page_name} | {url}")
        print(f"{page_id} | ❌ Erreur : {e}")
        print("--------------------------------")
    
