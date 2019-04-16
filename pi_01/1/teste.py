from info import InfoRequest
import requests

response = requests.get("http://google.com")
i = InfoRequest(response)
print(i.name)
print(i.protocol)
print(i.domain)