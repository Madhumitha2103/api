import requests
import json

def get_weather_data(city, date):
    url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q={}&appid=b6907d289e10d714a6e88b30761fae22&date={}".format(city, date)
    response = requests.get(url)
    data = json.loads(response.content)
    return data
