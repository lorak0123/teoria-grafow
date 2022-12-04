from copy import deepcopy

from controllers.poland_map_controller import show_poland_map
from controllers.poland_map_controller import show_poland_map_with_connections
from controllers.poland_cities_controller import read_data_from_file
from controllers.poland_cities_controller import get_random_cities
from config.constants import CITIES_RANDOM_COUNT
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree


# ETAP 1: wylosowanie miast i ich prezentacja na mapie

cities_in_poland = read_data_from_file()
random_cities = get_random_cities(cities_in_poland, CITIES_RANDOM_COUNT)
minimal_random_cities = deepcopy(random_cities)
show_poland_map(random_cities)

# ETAP 2: przypisanie do miast wszystkich możliwych sąsiadów

matrix = []
for city in random_cities:
    single_city_distances = []
    for city_2 in random_cities:
        single_city_distances.append(city.add_new_connection(city_2))
    matrix.append(single_city_distances)
show_poland_map_with_connections(random_cities)

# ETAP 3: wyliczenie minimalnego drzewa rozpinającego i prezentacja na mapie

X = csr_matrix(matrix)
Tcsr = minimum_spanning_tree(X)
res = Tcsr.toarray().astype(float)

for y in range(len(res)):
    for x in range(len(res[y])):
        if res[y][x] != 0:
            minimal_random_cities[y].add_new_connection(minimal_random_cities[x])

show_poland_map_with_connections(minimal_random_cities)

# ETAP 4: wyliczenie kosztów i uzyskanych oszczędności dzięki zastosowaniu algorytmu

sum_all_connections = sum([sum(i) for i in matrix]) / 2
sum_minimal_connections = sum(Tcsr.data)

print(f"Koszt utworzenia całej sieci połączeń między miastami: " +
      f"{sum_all_connections:.2f}")
print(f"Koszt minimalnego drzewa rozpinającego: " + 
      f"{sum_minimal_connections:.2f}")
print(f"Oszczędność dzięki zastosowaniu minimalnego drzewa rozpinającego: " +
      f"{(1-(sum_minimal_connections/sum_all_connections))*100:.2f}%")
