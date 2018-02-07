from bs4 import BeautifulSoup
import requests 
import time
import urllib

def getUrl():
    satrt_url = input()
    target_url = input()
    return satrt_url, target_url

def getHtml(Userurl):
    r = requests.get(Userurl)
    return r.text

def getFirstLink(htmlPart):
    article_link = None 
    soup = BeautifulSoup(htmlPart, 'html.parser')
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break

    if not article_link:
        return 

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link


def delay2Seconds(sec=2):
    time.sleep(sec)

def containsCycle(article_chain):
    if article_chain[-1] in article_chain[:-1]:
        return True
    return False

def continue_crawl(article_chain, target_url, max_steps=25):
    if article_chain[-1]==target_url:
        print("We reached the target url: "+target_url)
        return False

    if len(article_chain)>max_steps:
        print("We were unable to reach the target url after 25 attempts")
        return False

    if containsCycle(article_chain):
        print("We were unable to reach the target url because of falling in a loop")
        return False

    return True

if __name__ == '__main__':
    article_chain = []

    satrt_url, target_url = getUrl()
    article_chain.append(satrt_url)
    
    while continue_crawl(article_chain, target_url):
        print(article_chain[-1])
        html = getHtml(article_chain[-1])
        firstLink = getFirstLink(html)
        if not firstLink:
            print("We've arrived at an article with no links, aborting search!")
            break
        article_chain.append(firstLink)
        delay2Seconds()


