from controllers.poland_map_controller import show_poland_map
from controllers.poland_cities_controller import read_data_from_file, get_random_cities
from config.constants import CITIES_RANDOM_COUNT


# ETAP 1: wylosowanie miast i ich prezentacja na mapie

cities_in_poland = read_data_from_file()
random_cities = get_random_cities(cities_in_poland, CITIES_RANDOM_COUNT)
show_poland_map(random_cities)

# ETAP 2: przypisanie do miast wszystkich możliwych sąsiadów

for city in random_cities:
    for city_2 in random_cities:
        city.add_new_connection(city_2)
