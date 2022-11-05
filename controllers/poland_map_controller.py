import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from config.constants import RESOURCE_POLAND_MAP_PATH
from config.constants import MAP_GPS_LATITUDE_MAX
from config.constants import MAP_GPS_LATITUDE_MIN
from config.constants import MAP_GPS_LONGITUDE_MAX
from config.constants import MAP_GPS_LONGITUDE_MIN
from config.constants import MAP_PX_WIDTH_SIZE
from config.constants import MAP_PX_HEIGHT_SIZE
from config.constants import MAP_PX_HEIGHT_PADDING
from models.City import City


def calc_gps_to_pixels(lat: str, lon: str) -> tuple[int, int]:
    """
    Funkcja przelicza koordynaty GPS na konkretną pozycję na mapie Polski.

    :param lat: str: wysokość geograficzna w formacie GPS 00.000 °N
    :param lon: str: długość geograficzna w formacie GPS 00.000 °E
    :return: tuple[int, int] - współrzędne X, Y na wykresie
    """
    lat = lat.replace(" °N", "")
    lat = lat.replace(" °S", "")
    lon = lon.replace(" °W", "")
    lon = lon.replace(" °E", "")

    lat_f: float = float(lat)
    lon_f: float = float(lon)

    lat_f = ((lat_f - MAP_GPS_LATITUDE_MIN) / (MAP_GPS_LATITUDE_MAX - MAP_GPS_LATITUDE_MIN)) * MAP_PX_HEIGHT_SIZE
    lon_f = ((lon_f - MAP_GPS_LONGITUDE_MIN) / (MAP_GPS_LONGITUDE_MAX - MAP_GPS_LONGITUDE_MIN)) * MAP_PX_WIDTH_SIZE

    return int(lon_f), int(MAP_PX_HEIGHT_SIZE - lat_f + MAP_PX_HEIGHT_PADDING)


def show_poland_map(cities: list[City]) -> None:
    """
    Funkcja powoduje pokazanie na ekranie kompletnej mapy Polski bez dodatkowych oznaczeń.

    :param cities: list[City]: lista wylosowanych miast to prezentacji
    :return: None
    """
    poland_map = mpimg.imread(RESOURCE_POLAND_MAP_PATH, "jpg")
    plt.figure(figsize=(30, 30))

    for city in cities:
        x, y = calc_gps_to_pixels(city.latitude, city.longitude)
        plt.plot(x, y, marker='o', color="black")
        plt.text(x + 15.5, y + 4.5, city.name, fontsize=9)

    plt.imshow(poland_map)
    plt.show()
    return None


def show_poland_map_with_connections(cities: list[City]) -> None:
    """
    Funkcja pokazuje miasta na mapie Polski z uwzględnieniem połączeń pomiędzy nimi.

    :param cities: list[City]: lista wylosowanych miast to prezentacji
    :return: None
    """
    poland_map = mpimg.imread(RESOURCE_POLAND_MAP_PATH, "jpg")
    plt.figure(figsize=(30, 30))

    for city in cities:
        x, y = calc_gps_to_pixels(city.latitude, city.longitude)
        plt.plot(x, y, marker='o', color="black")
        plt.text(x + 15.5, y + 4.5, city.name, fontsize=9)

        for city_2 in city.get_city_connections():
            x1, y1 = calc_gps_to_pixels(city.latitude, city.longitude)
            x2, y2 = calc_gps_to_pixels(city_2.latitude, city_2.longitude)
            plt.plot([x1, x2], [y1, y2], color='black', marker='o', linestyle='solid', linewidth=1, markersize=1)

    plt.imshow(poland_map)
    plt.show()
    return None
