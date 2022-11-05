class City:
    """
    Klasa zawierająca informacje o miastach, które zostały wylosowane do projektu budowy szybkich dróg.
    """
    def __init__(self, name: str, latitude: str, longitude: str) -> None:
        self.name: str = name
        self.latitude: str = latitude
        self.longitude: str = longitude
        self.connected_cities: list = []

    def __str__(self) -> str:
        return f"City: { self.name }, latitude: { self.latitude }, longitude: { self.longitude }"
