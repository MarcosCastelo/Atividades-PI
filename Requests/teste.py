from request import *
from traveler import *

r = Request("https://google.com")
t = Traveler(r)

t.travel()
print(t.content.keys())