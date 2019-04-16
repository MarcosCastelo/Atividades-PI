class InfoRequest:
    def __init__(self, response):
        self.response = response
        pieces = self.response.url.split("//")
        self.protocol = pieces[0]
        rest = pieces[1].split(".")
        self.name = rest[1]
        self.domain = rest[-1]
        
        