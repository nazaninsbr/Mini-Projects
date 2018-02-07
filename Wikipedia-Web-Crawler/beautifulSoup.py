from bs4 import BeautifulSoup
import requests 
r = requests.get('http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html')
html = r.text
soup = BeautifulSoup(html, 'html.parser')
print(soup.p.a)