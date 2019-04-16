from search import Search

s = Search("Flamengo", "https://uol.com.br", 1)
s.search()
for key in s.results.keys():
    print(key, s.results[key])