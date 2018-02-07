from bs4 import BeautifulSoup
import requests 


def getUrl():
	url = input()
	return url

def getHtml(Userurl):
	r = requests.get(Userurl)
	return r.text

if __name__ == '__main__':
	x = getHtml(getUrl())
	print(x)