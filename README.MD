# Project: Interactive Map of Volcanoes and Population

This project creates an interactive map using the `folium` library in Python to display the location of volcanoes in Spain along with global population data. The map features two layers: one that shows volcanoes with color-coded markers based on elevation, and another that visualizes global population data using a GeoJSON file.

## Technologies and Libraries

- **Python**: The primary programming language used for data processing and visualization.
- **Folium**: A Python library used for generating interactive maps. Folium is built on the Leaflet.js library, which allows for easy map customization and layer control.
- **Pandas**: A Python library used for data manipulation and reading CSV files.
- **GeoJSON**: A format for encoding geographical data, used in this project to visualize global population statistics.

## Key Features

- **Volcano Visualization**: The map marks volcanoes in Spain using colored circular markers. Each marker displays the volcano’s name, location, and elevation. Marker colors change based on the elevation, providing quick insights into altitude variations.
- **Global Population Layer**: The map includes a layer that shows population distribution across countries using color coding. The population data is extracted from a **GeoJSON** file, and countries are colored based on their population size.
- **Interactive Map Controls**: Users can toggle between the volcano and population layers using a built-in layer control, enhancing the interactivity and data exploration.

## Files

- volcanoes_spain.txt: A CSV file containing information about volcanoes in Spain, with the following columns: Latitude, Longitude, Elevation (m), Name, Location.
- world.json: A GeoJSON file containing global population data.
- Map.html: The generated interactive map file.

## Code review

1. Data Loading
Volcano data from Spain is loaded from a CSV file, and the relevant columns are extracted for visualization on the map.

```
    import pandas as pd

    data = pd.read_csv("volcanoes_spain.txt")
    lat = list(data["Latitude"])
    lon = list(data["Longitude"])
    elev = list(data["Elevation (m)"])
    name = list(data["Name"])
    location = list(data["Location"])
```

2. Volcano Markers
Each volcano is marked on the map with a popup containing its name, location, and height. The color_producer function assigns colors to the markers based on the volcano's elevation.

```
    def color_producer(elevation):
        if elevation < 1000:
            return 'green'
        elif 1000 <= elevation < 3000:
            return 'orange'
        else:
            return 'red'
```
3. Adding Volcano Layer
A volcano feature group is created, adding a circular marker for each volcano with a popup showing the information.

```
    fgv = folium.FeatureGroup(name="Volcanoes")

    for lt, ln, el, nm, loc in zip(lat, lon, elev, name, location):
        iframe = folium.IFrame(html=html % (nm, loc, str(el)), width=250, height=150)
        fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))
```
4. Adding Population Layer
A population feature group is added, showing countries colored by their population size, based on data from the world.json file.

```
    fgp = folium.FeatureGroup(name="Population")

    fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else
                                                        'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
```
5. Building the Map
Both feature groups (volcanoes and population) are added to the map, and a layer control is included to switch between them.

```
    map = folium.Map(location=[41.735462, 1.82837], zoom_start=6, tiles="CartoDB positron")
    map.add_child(fgv)
    map.add_child(fgp)
    map.add_child(folium.LayerControl())
```
6. Saving the Map
Finally, the map is saved as an HTML file.
```
map.save("Map.html")
```

![](https://github.com/esmartdie/Map-Spain-Volcanoes/blob/main/Example.png)
