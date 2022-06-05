from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User, Concert, Feedback
from indie_app.models import Community
from django.http import JsonResponse
from .api import *
from .keys import (
    serviceId,
    AUTH_SECRET_KEY,
    AUTH_ACCESS_KEY,
    SMS_SEND_PHONE_NUMBER,
    )
import json

# Create your views here.

@login_required(login_url='/accounts/naver/login/')
def userpage(request):
    user = request.user
    return redirect('mypage', user.id)

@login_required(login_url='/accounts/naver/login/')
def mypage(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    people = User.objects.all()
    concerts = Concert.objects.all()
    community = Community.objects.all().order_by('-created_at')
    return render(request, 'mypage.html', {'person' : person, 'people': people, 'concerts': concerts, 'community': community})

@login_required(login_url='/accounts/naver/login/')
def transition(request):
    user = request.user
    if user.status == 0:
        user.status = 1
        user.save()
    else:
        user.status = 0
        user.save()
    return redirect('mypage', user.id)

@login_required(login_url='/accounts/naver/login/')
def edit(request):
    user = request.user
    if request.method == "GET":
        return render(request, "edit.html")
    else:
        user.name = request.POST['name']
        user.intro = request.POST['intro']
        user.insta = request.POST['insta']
        user.youtube = request.POST['youtube']
        try:
            user.image = request.FILES['image']
            user.save()
        except:
            user.save()
        return redirect('mypage', user.id)

@login_required(login_url='/accounts/naver/login/')
def follow(request, user_id):
    person = get_object_or_404(get_user_model(), id=user_id)
    if request.user in person.follower.all():
        person.follower.remove(request.user)
        person.save()
    else:
        person.follower.add(request.user)
        person.save()
    return redirect('mypage', user_id)

from allauth.socialaccount.models import SocialAccount

def callback(request):
    social_user = SocialAccount.objects.all()
    return render(request, 'callback.html', {'social_user' : social_user})

# 공연 등록 창
@login_required(login_url='/accounts/naver/login/')
def concert_form(request):
    return render(request, 'concert_form.html')

# 공연 등록 
@login_required(login_url='/accounts/naver/login/')
def concert_create(request):
    if(request.method == 'POST'):
        concert = Concert() 
        concert.musician = request.user
        concert.introduce = request.POST['introduce'] 
        concert.date = request.POST['date']
        concert.time = request.POST['time']
        concert.latitude = request.POST['latitude']
        concert.longitude = request.POST['longitude']
        concert.address = request.POST['address']
        concert.save() 
        social_user = SocialAccount.objects.all()
        # person = get_object_or_404(get_user_model(), id=request.user.id)
        for user in social_user:
            # if user in person.follower.all():  
            #     if user.alarm == 1:
                send_notification(concert.musician, concert.date, concert.time, concert.address, user.extra_data['mobile']) 
    return redirect('home')

@login_required(login_url='/accounts/naver/login/')
def feedback_form(request, user_id):
    if request.method == 'GET':
        person = get_object_or_404(get_user_model(), id=user_id)
        return render(request, 'feedback_form.html', {'person': person})
    else:
        feedback = Feedback()
        feedback.feedback_post = get_object_or_404(get_user_model(), id=user_id)
        feedback.feedback_name = request.user.name
        feedback.feedback_profile = request.user.image
        feedback.feedback_content = request.POST["feedback_content"]
        feedback.feedback_image = request.FILES.get('feedback_image')
        feedback.save()
        return redirect('mypage', user_id)

