import requests

r = requests.get("https://newsapi.org/v1/sources?category=general")
#print(r.json())
sources = r.json()["sources"]

ids = []
for source in sources:
    ids.append(source["id"])

print(ids)