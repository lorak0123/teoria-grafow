from controllers.poland_map_controller import show_poland_map
from controllers.poland_cities_controller import read_data_from_file, get_random_cities


cities_in_poland = read_data_from_file()
random_cities = get_random_cities(cities_in_poland, 50)
show_poland_map(random_cities)
