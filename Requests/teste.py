from request import *
from traveler import *

r = Request("https://www.google.com.br/intl/pt-BR/policies/privacy/")
t = Traveler()

t.travel(r,1)
print(t.content.keys())