from pws import WeatherMap_IP 

import requests
from pprint import pprint

#API_Key = WeatherMap_IP
city = input("Enter a City: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+WeatherMap_IP+"&q="+city
weather_data = requests.get(base_url).json()

pprint(weather_data)