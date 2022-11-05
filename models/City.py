from __future__ import annotations


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
        return f"City: { self.name }, latitude: { self.latitude }, longitude: { self.longitude }"

    def add_new_connection(self, add_city: City) -> None:
        """
        Dodaje do miasta informację o połączonych z nim innymi miastami.

        :param add_city: City: miasto połączone z aktualnym miastem
        :return: None
        """
        self.__connected_cities.append(add_city)
        return None
