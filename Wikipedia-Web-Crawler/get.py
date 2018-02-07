import requests 
r = requests.get('http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html')
webPage = r.text
print(webPage)