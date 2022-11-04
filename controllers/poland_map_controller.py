import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from config.constants import RESOURCE_POLAND_MAP_PATH
from models.City import City


def calc_gps_to_pixels(lat: str, lon: str) -> tuple[int, int]:
    """
    Funkcja przelicza koordynaty GPS na konkretną pozycję na mapie Polski.

    :param lat: str: wysokość geograficzna w formacie GPS 00.000 °N
    :param lon: str: szerokość geograficzna w formacie GPS 00.000 °E
    :return: tuple[int, int] - współrzędne X, Y na wykresie
    """
    return 50, 50


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
        plt.text(x + .03, y + .03, city.name, fontsize=9)

    plt.imshow(poland_map)
    plt.show()
    return None
