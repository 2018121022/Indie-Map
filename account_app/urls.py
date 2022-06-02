from django.urls import path
from .views import *

urlpatterns = [
    path('', userpage, name="userpage"),
    path('mypage/<int:user_id>', mypage, name="mypage"),
    path('transition/', transition, name="transition"),
    path('edit/', edit, name="edit"),
]