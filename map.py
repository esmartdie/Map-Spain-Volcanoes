import folium
import pandas as pd

data = pd.read_csv("volcanoes_spain.txt")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elevation (m)"])
name = list(data["Name"])
location = list(data["Location"])

html = """
<h4>Volcano information:</h4>
<strong>Name:</strong> %s<br>
<strong>Location:</strong> %s<br>
<strong>Height:</strong> %s m
"""

def color_producer(elevation):
    if(elevation<1000):
        return 'green'
    elif(elevation<= elevation < 3000):
        return 'orange'
    else:
        return 'red'

map=folium.Map(
    location=[41.73546232379051, 1.8283699478719764],
    zoom_start=9, 
    tiles = "CartoDB positron")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nm, loc in zip(lat, lon, elev, name, location):
    iframe = folium.IFrame(html=html % (nm, loc, str(el)), width=250, height=150)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), 
                                     fill_color=color_producer(el), color='grey', fill_opacity=0.7))
    
fg=folium.FeatureGroup(name="Population")
    
fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']< 10000000 else 
                            'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map.html")