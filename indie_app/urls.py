from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('mypage_1/', mypage_1, name="mypage_1"),
    path('mypage_2/', mypage_2, name="mypage_2"),
    path('mypage_3/', mypage_3, name="mypage_3"),
    path('musicpage_1/', musicpage_1, name="musicpage_1"),
    path('musicpage_2/', musicpage_2, name="musicpage_2"),
    path('musicpage_3/', musicpage_3, name="musicpage_3"),
    path('transition/', transition, name="transition"),
    path('new/', new, name="new"),
    path('detail/<int:community_id>/', detail, name="detail"),
    path('community/', community, name="community"),
    path('like/<int:community_id>/', like, name="like"),
    path('search/', search, name="search"),
    path('musician_list/', musician_list, name="musician_list"),
    path('comment/<int:community_id>/', comment, name="comment"),
    path('calendar/', calendar, name="calendar"),
]