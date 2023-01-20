#!/usr/bin/python3

import requests
import json
import sys

URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()[0:32]

def get_data(city):
    url = "{URL}q={city}&appid={API}".format(URL=URL, API=API_KEY, city=city)
    response=requests.get(url).json()
    temperature = response['main']['temp'] - 273.15
    print(f"Temperature in {city}: {temperature}")


if __name__ == "__main__":
    city = str(sys.argv[1])
    get_data(city)
