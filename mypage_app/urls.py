from django.urls import path
from .views import *

urlpatterns = [
    path('', mypage_1, name="mypage_1"),
    path('mypage_2/', mypage_2, name="mypage_2"),
    path('mypage_3/', mypage_3, name="mypage_3"),
    path('musicpage_1/', musicpage_1, name="musicpage_1"),
    path('musicpage_2/', musicpage_2, name="musicpage_2"),
    path('musicpage_3/', musicpage_3, name="musicpage_3"),
]