from request import Request
import requests

class Traveler:
    def __init__(self):
        self.content = {}

    
    def travel(self, request: Request, depth=0):
        links = request.getLinks()
        if depth == 0:
            if links != None:
                for link in request.getLinks():
                    print(link, depth)
                    r = Request(link)
                    if r.isValidated and link not in self.content.keys():
                        self.content.update({link : r.content})
        else:
            if links != None:
                for link in request.getLinks():
                    print(link, depth)
                    r = Request(link)
                    if r.isValidated and link not in self.content.keys():
                        self.content.update({link : r.content})
                        self.travel(r, depth - 1)
            

