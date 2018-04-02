from urllib.parse import urlparse

def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2]+ '.' +results[-1]
	except:
		return ''

def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''


#print(get_domain_name('https://www.youtube.com/watch?v=PPonGS2RZNc&index=14&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q'))