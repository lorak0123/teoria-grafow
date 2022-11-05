import random
import pandas as pd
from typing import List
from models.City import City
from config.constants import RESOURCE_POLAND_CITIES


def read_data_from_file() -> List[City]:
    df = pd.read_excel(RESOURCE_POLAND_CITIES, header=1).iloc[:, 0:3]

    cities:List[City] = []

    for index, row in df.iterrows():
        city = City(row['Miasto'], row['Szerokość'], row['Długość'])
        cities.append(city)

    return cities


def get_random_cities(cities: List[City], amount: int) -> List[City]:
    return random.choices(cities, k=amount)