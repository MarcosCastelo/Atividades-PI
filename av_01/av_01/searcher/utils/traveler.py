from request import *
import requests

class Traveler:
    def __init__(self):
        self.content = {}

    
    def travel(self, request: Request, depth=0):
        links = request.getLinks()
        if depth == 0:
            self.content.update({request : 0})
                
                            
        else:
            if links != None:
                for link in request.getLinks():
                    print(link, depth)
                    r = Request(link)
                    if r.isValidated :
                        if link not in self.content.keys():
                            self.content.update({r : 0})
                            self.travel(r, depth - 1)
                        else:
                            self.content[r] += 1
                        
                        
            

