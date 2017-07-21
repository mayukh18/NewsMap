from geograpy import get_place_context

def get_place(title, desc, url):
    if desc != None:
        text = title + desc
    else:
        text = title
    places = get_place_context(text=text)
    if len(places.cities) > 0:
        return places.cities[0]
    elif len(places.countries) > 0:
        return places.countries[0]

    places = get_place_context(url= url)
    if len(places.cities) > 0:
        return places.cities[0]
    elif len(places.countries) > 0:
        return places.countries[0]

    return 0

