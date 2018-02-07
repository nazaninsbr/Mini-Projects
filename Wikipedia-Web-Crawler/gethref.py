from bs4 import BeautifulSoup
import requests 
r = requests.get('https://en.wikipedia.org/wiki/Wikipedia')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.p.a)