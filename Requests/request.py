import requests
import requests_cache
from bs4 import BeautifulSoup

class Request:
    def __init__(self, url):
        self.url = None
        self.response = None
        self.content = None
        response = None
        try:
            response = requests.get(url)
        except:
            pass
        if response != None:
            if response.status_code == 200:
                self.url = url
                self.response = response
                self.content = response.content
    

    def isValidated(self):
        if self.response != None:
            return True
            
        return False


    def getLinks(self, onlyBody=True):
        soup = BeautifulSoup(self.content, 'html.parser')
        links = []
        if onlyBody:
            for link in soup.body.find_all('a'):
                links.append(link['href'])
            return links

        for link in soup.find_all('a'):
            links.append(link['href'])


    def getContent(self):
        return self.content

    def getUrl(self):
        return self.url