from django.urls import path
from .views import *

urlpatterns = [
    path('', userpage, name="userpage"),
    path('mypage/<int:user_id>', mypage, name="mypage"),
    path('transition/', transition, name="transition"),
    path('edit/', edit, name="edit"),
    path('scrap/<int:user_id>', follow, name="follow"),
    path('concert_form/', concert_form, name="concert_form"),
    path('concert_create/', concert_create, name='concert_create'),
    path('feedback/<int:user_id>', feedback_form, name="feedback_form"),
    path('alarm/', alarm, name="alarm"),
    path('highlight/<int:user_id>', highlight, name="highlight"),
    path('highlight_detail/<int:high_id>', highlight_detail, name="highlight_detail"),
]