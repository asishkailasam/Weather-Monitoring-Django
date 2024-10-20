from celery import shared_task
from .services import fetch_weather_data

@shared_task
def fetch_weather_for_cities():
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    for city in cities:
        fetch_weather_data(city)
