from django.urls import path
from .views import *

urlpatterns = [
    path('', map, name="map"),
    path('login/', login_map, name="login_map"),
    path('each/', each_map, name="each_map"),
    path('concertInput/', concert_input, name="concert_input"),
]