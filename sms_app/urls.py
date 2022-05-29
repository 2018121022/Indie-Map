from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns 

urlpatterns = [
    path('', sms, name="sms"),
    path('alarm_sms/', alarm_sms, name="alarm_sms")
]

urlpatterns = format_suffix_patterns(urlpatterns) 