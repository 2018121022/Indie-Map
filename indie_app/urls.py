from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('new/', new, name="new"),
    path('detail/<int:community_id>/', detail, name="detail"),
    path('community/', community, name="community"),
    path('like/<int:community_id>/', like, name="like"),
    path('search/', search, name="search"),
    path('musician_list/', musician_list, name="musician_list"),
    path('comment/<int:community_id>/', comment, name="comment"),
    path('calendar/', calendar, name="calendar"),
    path('faq/',faq,name="faq"), #jian
]