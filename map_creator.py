import config
import requests
import os
import random
from helpers import get_place
import folium


SOURCES_URL = os.environ.get('NEWSAPI_SOURCES_URL', config.NEWSAPI_SOURCES_URL)
ARTICLES_URL = os.environ.get('NEWSAPI_ARTICLES_URL', config.NEWSAPI_ARTICLES_URL)
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', config.GOOGLE_MAPS_API_KEY)
key = os.environ.get('NEWSAPI_KEY', config.NEWSAPI_KEY)

map = folium.Map(location=[10, 0], zoom_start=2.1)

r = requests.get(SOURCES_URL+"?category=general&language=en")
sources = r.json()["sources"]
ids = []
for source in sources:
    ids.append(source["id"])

world_news = []
print(ids)
ids.remove('associated-press')
print(ids)
for id in ids:
    print(id)
    news = requests.get(ARTICLES_URL+"?source="+id+"&sortBy=top&apiKey="+key)
    news = news.json()
    news = news["articles"]
    for article in news:
        url = article["url"]
        title = article["title"]
        desc = article["description"]
        print(title)

        location = get_place(title, desc, url)
        print(location)
        if location == 0:
            continue

        loc = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + location + '&key=' + GOOGLE_MAPS_API_KEY)
        loc = loc.json()

        if loc["status"] != "OK":
            continue

        lat = loc["results"][0]["geometry"]["location"]["lat"] + round(random.uniform(0.05, 0.1), 6)
        lng = loc["results"][0]["geometry"]["location"]["lng"] + round(random.uniform(0.05, 0.12), 6)

        print(lat, lng)
        #folium.RegularPolygonMarker([lat, lng], popup=title,
        #                            fill_color='#456488', number_of_sides=5, radius=10).add_to(map)
        folium.Marker([lat, lng], popup=desc).add_to(map)

        world_news.append({"title": title, "lat":lat, "lng":lng})

map.save(outfile='worldnews.html')