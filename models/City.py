class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latidude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return f"City: {self.name}, latitude: {self.latidude}, longitude: {self.longitude}"