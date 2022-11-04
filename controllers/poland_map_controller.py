import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from config.constants import RESOURCE_POLAND_MAP_PATH
from config.constants import MAP_GPS_LATITUDE_MAX
from config.constants import MAP_GPS_LATITUDE_MIN
from config.constants import MAP_GPS_LONGITUDE_MAX
from config.constants import MAP_GPS_LONGITUDE_MIN
from config.constants import MAP_PX_WIDTH_SIZE
from config.constants import MAP_PX_HEIGHT_SIZE
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

    width_scale: float = MAP_PX_WIDTH_SIZE / (MAP_GPS_LONGITUDE_MAX - MAP_GPS_LONGITUDE_MIN)
    height_scale: float = MAP_PX_HEIGHT_SIZE / (MAP_GPS_LATITUDE_MAX - MAP_GPS_LATITUDE_MIN)

    lat_f = (lat_f - MAP_GPS_LATITUDE_MIN) * height_scale
    lon_f = (lon_f - MAP_GPS_LONGITUDE_MIN) * width_scale

    return int(lat_f), int(lon_f)


def show_poland_map(cities: list[City]) -> None:
    """
    Funkcja powoduje pokazanie na ekranie kompletnej mapy Polski bez dodatkowych oznaczeń.

    :return: None
    """
    poland_map = mpimg.imread(RESOURCE_POLAND_MAP_PATH, "jpg")
    plt.figure(figsize=(30, 30))

    for city in cities:
        x, y = calc_gps_to_pixels(city.latidude, city.longitude)
        plt.plot(x, y, marker='o', color="black")
        plt.text(x + 15.5, y - 4.5, city.name, fontsize=9)
        print([city.name, city.longitude, city.latidude, str(x) + " px", str(y) + " px"])

    plt.imshow(poland_map)
    plt.show()
    return None
