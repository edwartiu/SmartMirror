import pickle
import json
import requests


def get_weather():
    zip_code = '90002'
    api_key = None
    with open('weather_token.pkl', 'rb') as token:
        api_key = pickle.load(token)
    api_call = "http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}&units=imperial".format(zip_code, api_key)

    response = requests.get(api_call)
    response = response.json()

    weather = {}
    weather['temp'] = response["main"].get('temp')
    weather['description'] = response['weather'][0].get('description')
    weather['icon'] = response['weather'][0].get('icon')
    weather['city'] = response.get('name')
    
    return weather
