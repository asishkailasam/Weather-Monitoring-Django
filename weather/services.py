import requests
from django.conf import settings
from .models import WeatherData

def fetch_weather_data(city):
    api_key = settings.OPENWEATHERMAP_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    WeatherData.objects.create(
        city=city,
        temperature=data['main']['temp'],
        feels_like=data['main']['feels_like'],
        condition=data['weather'][0]['main'],
        timestamp=data['dt']
    )
    return data
