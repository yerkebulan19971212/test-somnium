import requests
from collections import Counter
from bs4 import BeautifulSoup
url = 'http://127.0.0.1:8000/obmennik/curs_valuta/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
tags = [tag.name for tag in soup.find_all()]

counter = Counter(tags)


print(counter.values())
