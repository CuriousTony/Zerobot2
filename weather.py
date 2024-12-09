import requests
from os import getenv

WEATHER_TOKEN = getenv('WEATHER_TOKEN')
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'


async def get_weather(city):
    try:
        params = {
            'q': city,
            'appid': WEATHER_TOKEN,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(WEATHER_URL, params=params)
        data = response.json()

        if data.get('cod') != 200:
            return "Город не найден. Пожалуйста, проверьте название."

        city_name = data['name']
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']

        return f"Погода в {city_name}: {weather_description}, {temp}°C"
    except Exception as e:
        return f"Ошибка при получении данных: {e}"
