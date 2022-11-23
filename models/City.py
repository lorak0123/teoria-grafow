from __future__ import annotations

from math import radians, cos, sin, asin, sqrt


class City:
    """
    Klasa zawierająca informacje o miastach, które zostały wylosowane do projektu budowy szybkich dróg.
    """

    def __init__(self, name: str, latitude: str, longitude: str) -> None:
        self.name: str = name
        self.latitude: str = latitude
        self.longitude: str = longitude
        self.__connected_cities: list[City] = []

    def __str__(self) -> str:
        """
        Zwraca tekstowy opis klasy miasta z najważniejszymi informacjami o nim.

        :return: str
        """
        return f"City: {self.name}, latitude: {self.latitude}, longitude: {self.longitude}"

    def add_new_connection(self, add_city: City) -> float:
        """
        Dodaje do miasta informację o połączonych z nim innymi miastami.

        :param add_city: City: miasto połączone z aktualnym miastem
        :return: None
        """
        if self.name is not add_city.name:
            self.__connected_cities.append(add_city)
            return self.calculate_distance(add_city)
        return 0

    def get_city_connections(self) -> list[City]:
        """
        Funkcja zwraca informacje o wszystkich miastach połączonych z danym miastem.

        :return: list[City]
        """
        return self.__connected_cities

    def calculate_distance(self, other: City) -> float:
        """
        Funkcja zwraca odległość miasta od drugiego

        :return: float
        """
        lat1 = radians(float(self.latitude.replace(" °N", "")))
        lon1 = radians(float(self.longitude.replace(" °E", "")))
        lat2 = radians(float(other.latitude.replace(" °N", "")))
        lon2 = radians(float(other.longitude.replace(" °E", "")))

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        # calculate the result
        return (c * r)
