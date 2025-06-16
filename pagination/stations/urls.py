from django.urls import path
from .views import bus_stations

urlpatterns = [
    path('', bus_stations, name='bus_stations')
]
