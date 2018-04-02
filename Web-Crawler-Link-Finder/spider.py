from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:

	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = '' 
	queue = set()
	crawled = set()

	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.project_name+"/queue.txt"
		Spider.crawled_file = Spider.project_name+"/crawled.txt"
		self.boot()
		self.crawl_page('First spider', Spider.base_url)

	@staticmethod
	def boot():
		create_project_dir(Spider.project_name)
		create_data_files(Spider.project_name, Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)


	@staticmethod
	def crawl_page(spiderName, pageUrl):
		if pageUrl not in Spider.crawled:
			print(spiderName+ ' now crawling: ' +pageUrl)
			print('Queue: '+str(len(Spider.queue)) + ' | Crawled: '+str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_links(pageUrl))
			Spider.queue.remove(pageUrl)
			Spider.crawled.add(pageUrl)
			Spider.update_files()

	@staticmethod
	def gather_links(pageUrl):
		html_string = ''
		try:
			response = urlopen(pageUrl)
			if 'text/html' in response.getheader('Content-Type'):
				html_bytes = response.read()
				print('html bytes')
				print(html_bytes)
				html_string = html_bytes.decode('utf-8')
			finder = LinkFinder(Spider.base_url, pageUrl)
			finder.feed(html_string)
		except:
			print('Error: can not crawl page')
			return set()

		return finder.page_links()


	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue 
			if url in Spider.crawled:
				continue
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def update_files():
		set_to_file(Spider.queue_file, Spider.queue)
		set_to_file(Spider.crawled_file, Spider.crawled)









