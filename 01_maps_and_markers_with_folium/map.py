import os
import csv
import folium
import folium.plugins as plugins

def gather_location_data() -> dict:
    # Get CSV rows
    with open('data.csv', mode='r') as csv_file:
        _locations = {} # {(lat,long) count}
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            lat_long = (row["latitude"], row["longitude"])
            if lat_long in _locations:
                _locations[lat_long] += 1
            else:
                _locations[lat_long] = 1
    return _locations

def numeric_marker(lat_long=tuple, number=int) -> folium.Marker:
    icon_details = plugins.BeautifyIcon(
        icon_shape="marker",
        border_color="#FF0000",
        background_color="#FFFFFF",
        text_color="#000000",
        number=number
        )
    marker = folium.Marker(
        location=lat_long,
        icon=icon_details
    )
    return marker

def save_to_file(folium_map=folium.map, file_name=str):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    folium_map.save(file_name)

def add_location_markers(folium_map=folium.map, locations=dict):
    for lat_long,count in locations.items():
        numeric_marker(lat_long, count).add_to(folium_map)


if __name__ == "__main__":
    m = folium.Map(location=[37, -97.5], zoom_start=5, tiles="OpenStreetMap")
    locations = gather_location_data()
    add_location_markers(folium_map=m, locations=locations)
    save_to_file(m, "output/map.html")
