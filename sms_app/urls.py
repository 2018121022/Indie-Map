from django.urls import path
from .views import *

urlpatterns = [
    path('', sms, name="sms"),
]