from django.urls import path
from .views import *

urlpatterns = [
    path('', map, name="map"),
    path('login/', login_map, name="login_map"),
    
   
]