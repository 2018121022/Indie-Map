from tokenize import maybe
from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', account, name="account"),
    path('callback/',callback,name='callback')
    #path('/account',account,name="account"),
    #path('/admin', admin.site.urls),
]