from request import Request
import requests

class Traveler:
    def __init__(self, request: Request):
        self.request = request
        self.content = {}

    
    def travel(self):
        for link in  self.request.getLinks():
            r = Request(link)
            if r.isValidated and link not in self.content.keys():
                self.content.update({link : r.content})
