import folium
import pandas
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

geolocator = Nominatim(user_agent="specify_your_app_name_here")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=4)


def find_by_year(str_year):
    """
    (str)->list
    Returns list of lines from file where the name of year appears.
    """
    year_in_line_list = []
    file = open('locations.csv', 'r', encoding='utf-8', errors='ignore')
    for x in file:
        if str_year in x:
            year_in_line_list.append(x)
    return year_in_line_list


def get_film_info(file_lines):
    """
    (list)->(dict)
    Returns a dictionary with names = keys,locations = values taken from lines in file.
    """
    films_info = {}
    for line in file_lines:
        line = line.strip().split(',')
        location = line[-1]
        if location and location != 'NO DATA':
            films_info[line[0]] = location
    return films_info


def get_geo_parameters(film_info, layer_name):
    """
    (dict,str)
    Decodes locations and add markers on map for this locations and movies filmed there.
    """
    for key, value in film_info.items():
        geodecoded = geolocator.geocode(value)
        if geodecoded:
            print(key)
            coordinates_list = [geodecoded.latitude, geodecoded.longitude]
            layer_name.add_child(folium.Marker(location=coordinates_list,
                                               popup=key,
                                               icon=folium.Icon()))


def filmed_amount():
    """
    None->(dict)
    Reads a file and takes all locations from it.
    Returns a dictionary with keys = locations,values = amount of movies filmed there.
    """
    locations_by_frequency = []
    by_frequency_dict = {}
    top_locations_dict = {}
    locations_data = pandas.read_csv("locations.csv", error_bad_lines=False)
    locations = locations_data['location']
    for item in locations:
        if item != 'NO DATA':
            if item in by_frequency_dict:
                by_frequency_dict[item] += 1
            else:
                by_frequency_dict[item] = 1
    sorted(by_frequency_dict.items(), key=lambda x: x[1])
    for key, value in by_frequency_dict.items():
        if value > 1000:
            locations_by_frequency.append((key, value))
        locations_by_frequency.sort(key=lambda x: x[1])

    for el in locations_by_frequency[-50:]:
        top_locations_dict[el[0]] = el[1]

    return top_locations_dict


def color_def(amount):
    """
    (int)-> str
    Returns color of circle depending on amount of films for location.
    >>> color_def(25156)
    'red'
    >>> color_def(8500)
    'lightsalmon'
    """

    if amount < 10000:
        return "lightsalmon"
    elif 10000 <= amount < 20000:
        return "orangered"
    elif 20000 <= amount <= 30000:
        return "red"
    else:
        return "darkred"


def most_filmed_layer(top_locations):
    """
    (dict)->None
    Gets geo-coordinates for top 50  locations and adds circle markers on the map for them.
    """
    fg_am = folium.FeatureGroup(name="Most popular")
    for key, value in top_locations.items():
        parameters = geolocator.geocode(key)
        coordinates = [parameters.latitude, parameters.longitude]
        if coordinates:
            fg_am.add_child(folium.CircleMarker(location=coordinates,
                                                radius=7,
                                                popup=key + "\n" + str(value),
                                                fill_color=color_def(int(value)),
                                                color=color_def(int(value)),
                                                fill_opacity=0.5))
        map.add_child(fg_am)


map = folium.Map(zoom_start=10)

fg_1939 = folium.FeatureGroup(name="Start of 2 world war")
fg_1945 = folium.FeatureGroup(name="Middle of 2 world war")

file_lines_1939 = find_by_year('1939')
file_lines_1945 = find_by_year('1945')

film_data_1939 = get_film_info(file_lines_1939)
film_data_1945 = get_film_info(file_lines_1945)

get_geo_parameters(film_data_1939, fg_1939)
get_geo_parameters(film_data_1945, fg_1945)

top_locations_list = filmed_amount()
most_filmed_layer(top_locations_list)

map.add_child(fg_1939)
map.add_child(fg_1945)


map.add_child(folium.LayerControl())
map.save('Map_World_War2.html')
