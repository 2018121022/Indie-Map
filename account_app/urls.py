from django.urls import path
from .views import *

urlpatterns = [
    path('', userpage, name="userpage"),
    path('mypage/<int:user_id>', mypage, name="mypage"),
    path('transition/', transition, name="transition"),
    path('edit/', edit, name="edit"),
    path('scrap/<int:user_id>', follow, name="follow"),
    path('callback/', callback, name="callback"),
    path('concert_form/', concert_form, name="concert_form"),
    path('concert_create/', concert_create, name='concert_create'),
]