from tokenize import maybe
from django.urls import path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', account, name="account"),
    path('callback/',callback,name='callback'),
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name = "logout"),
    path('register/', register_view, name="signup"),
    #path('/account',account,name="account"),
    #path('/admin', admin.site.urls),
]