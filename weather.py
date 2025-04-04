import requests

APIKEY = "79d1ca96933b0328e1c7e3e7a26cb347"


def weather_finder(city=None, wlat=200, wlon=200):
    if city is not None:
        city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={APIKEY}"
        try:
            wlat = requests.get(city_url).json()[0]["lat"]
            wlon = requests.get(city_url).json()[0]["lon"]
        except IndexError:
            return "Check city's name or send it by geolocation"

    responce = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={wlat}&lon={wlon}&units=metric&exclude=current&lang=en&appid={APIKEY}"
    )
    data = responce.json()

    city_name = data["name"].capitalize()
    icon = data["weather"][0]["icon"][:2]
    desc = data["weather"][0]["main"].lower()
    temp = data["main"]["temp"]
    temp_fells = data["main"]["feels_like"]

    emojis = {
        "01": "☀️",
        "02": "⛅",
        "03": "☁️",
        "04": "☁️",
        "09": "🌧️",
        "10": "🌦️",
        "11": "⛈️",
        "13": "🌨️",
        "50": "☁️",
    }

    return f"{emojis[icon]} In {city_name} there is {desc}.\nTemperture is {temp}℃, feels like {temp_fells}℃."


#def find_city(lat, lon):
    #url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&appid=79d1ca96933b0328e1c7e3e7a26cb347"
    #return requests.get(url).json()[0]['name']

#dresponce = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat=55.76157243730561&lon=37.58638282525473&units=metric&exclude=current&lang=en&appid=79d1ca96933b0328e1c7e3e7a26cb347")
#ddata = dresponce.json()
#print(ddata['name'].capitalize())