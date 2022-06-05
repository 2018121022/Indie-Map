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
    path('feedback/<int:user_id>', feedback_form, name="feedback_form"),
    path('alarm/', alarm, name="alarm"),
    path('delete_post/<int:post_id>', delete_post, name="delete_post"),
    path('modify_post/<int:post_id>', modify_post, name="modify_post"),
    path('delete_feedback/<int:feedback_id>', delete_feedback, name="delete_feedback"),
    

]