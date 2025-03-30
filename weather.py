from http.client import responses

import requests
import json


def weather_finder(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&exclude=current&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    try:
        responce = requests.get(url)
        data = responce.json()
        icon = data['weather'][0]['icon'][:2]
        main_weth = data["weather"][0]['main'].lower()
        temp = data['main']['temp']
        temp_fells = data['main']['feels_like']
    except:
        return "Error, check if name is correct"

    emojis = {"01" : "☀️", "02" : "⛅", "03" : "☁️", "04" : "☁️", "09" : "🌧️", "10" : "🌦️", "11" : "⛈️", "13" : "🌨️", "50" : "☁️",}

    return f"{emojis[icon]} In {city.capitalize()} there is {main_weth}.\nTemperture is {temp}℃, feels like {temp_fells}℃."

def find_city(lat, lon):
    url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid=79d1ca96933b0328e1c7e3e7a26cb347"
    return requests.get(url).json()[0]['name']





