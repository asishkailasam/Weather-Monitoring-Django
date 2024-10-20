from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default view for weather home
    path('summary/', views.weather_summary, name='weather_summary'),  # Weather summary view
    path('alerts/', views.weather_alerts, name='weather_alerts'),  # Weather alerts view
]
