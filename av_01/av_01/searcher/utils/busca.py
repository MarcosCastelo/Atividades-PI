import requests
from bs4 import BeautifulSoup
import re

class Url_Validator:
    def __init__(self, url):
        self.url = url
        self.protocol = ""
        self.link = []
        if url != None:
            parts = self.url.split("//")
            self.protocol = parts[0]
            if len(parts) > 1:
                self.link = parts[1].split(".")

        if len(self.link) < 2 or self.protocol == "":
            self.url = ""
       

    def __str__(self):
        return self.url

    def __repr__(self):
        return self.url


def search(keyword : str, url, depth : int):
    url_o = Url_Validator(url)
    if url_o != None:
        response = requests.get(url_o)
        links = link_parser(response.text)
        all_pages = travel_depth(links, depth)
        results = []

        for page in all_pages:
            results.append(key_parser(page, keyword))
        print(results)
        

def link_parser(text : str):
    links = []
    soup = BeautifulSoup(text, 'html.parser')
    for link in soup.find_all('a'):
        link_validated = Url_Validator(link.get('href'))
        if link_validated.url != "":
            print(link_validated)
            links.append(link_validated)
    return links
    

def key_parser(text: str, key : str):
    soup = BeautifulSoup(text, 'html.parser')
    results = soup.text.find_all(string=re.compile('.*{0}.*'.format(key)), recursive=True)
    return results

def travel_depth(links, depth):
    pages = []
    links_visited = []
    if depth == 0:
        return pages
    else:
        for link in links:
            if link not in links_visited:
                links_visited.append(link)
                response = requests.get(link)
                pages.append(response.text)
                o_links = link_parser(response.text)
                depth -= 1
                travel_depth(o_links, depth)
            else:
                continue

search("cu", "http://xvideos.com", 1)