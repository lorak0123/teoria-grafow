import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from config.constants import RESOURCE_POLAND_MAP_PATH
from models.City import City


def show_poland_map(cities: list[City]) -> None:
    """
    Funkcja powoduje pokazanie na ekranie kompletnej mapy Polski bez dodatkowych oznaczeń.

    :return: None
    """
    poland_map = mpimg.imread(RESOURCE_POLAND_MAP_PATH, "jpg")
    plt.figure(figsize=(30, 30))
    plt.imshow(poland_map)
    plt.show()
    return None
