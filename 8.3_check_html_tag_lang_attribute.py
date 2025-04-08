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
        html_tag = soup.find('html')
        lang = html_tag.get('lang') if html_tag else '❌ Pas de balise <html>'
        
        print(f"{page_id} | {page_name} | {url}")
        print(f"{page_id} | 8.3 - html[lang] : {'✅ ' + lang if lang else '❌ Non spécifié'}")
        print("--------------------------------")
    except Exception as e:
        print(f"{page_id} | {page_name} | {url}")
        print(f"{page_id} | ❌ Erreur : {e}")
        print("--------------------------------")
    
