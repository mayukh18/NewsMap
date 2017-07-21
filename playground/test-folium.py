import folium
from folium.plugins import Fullscreen

m = folium.Map(location=[10, 0], zoom_start=2.1)
Fullscreen().add_to(m)

m.save(outfile='fullscreen.html')


import geograpy
url = 'http://www.bbc.com/news/world-europe-26919928'
places = geograpy.get_place_context(url=url)

folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows').add_to(m)