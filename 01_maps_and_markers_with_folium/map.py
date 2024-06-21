import folium
import folium.plugins as plugins
import csv

m = folium.Map(location=[37, -97.5], zoom_start=5, tiles="OpenStreetMap")

def gather_location_data() -> dict:
    # Get CSV rows
    with open('data.csv', mode='r') as csv_file:
        locations = {} # {(lat,long) count}
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            lat_long = (row["lat"], row["long"])
            if (lat_long) in locations:
                locations[lat_long] += 1
            else:
                locations[lat_long] = 1
    return locations

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

def save_to_file(item=any,file_name=str):
    html = item._repr_html_()
    file1 = open(file_name, 'w')
    file1.write(html)
    file1.close()

locations = gather_location_data()
for lat_long,count in locations.items():
    numeric_marker(lat_long, count).add_to(m)

save_to_file(m, "map.html")
