from request import *
from traveler import *
from bs4 import BeautifulSoup
import re

class Search:
    def __init__(self, keyword: str, url: str, depth: int):
        self.url = url
        self.keyword = keyword
        self.depth = depth
        self.results = {}

        self.traveler = Traveler()
        self.request = Request(self.url)
        

    def search(self):
        if self.request.isValidated():
            self.traveler.travel(self.request, self.depth)
            for key in self.traveler.content.keys():
                if key.content != None: 
                    result = self.find_key(key.content)
                    if result != [] and result != None:
                        self.results.update({key.url : result})

        else:
            print("Fora do ar")


        
    def find_key(self, content):
        soup = BeautifulSoup(content, 'html.parser', from_encoding="iso-8859-1")
        try:
            return soup.body.find_all(string=re.compile('.*{0}.*'.format(self.keyword)), recursive=True)
        except:
            pass




