from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from allauth.socialaccount.models import SocialAccount
from .models import User, Concert, Feedback, Highlight
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
from django.utils import timezone


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
    feedback_set = Feedback.objects.filter(feedback_post = person).order_by('-feedback_time')
    highlight_set = Highlight.objects.filter(uploader = person).order_by('-highlight_time')
    return render(request, 'mypage.html', {'person' : person, 'people': people, 'concerts': concerts, 
    'community': community, 'feedback_set' : feedback_set, 'highlight_set' : highlight_set })

@login_required(login_url='/accounts/naver/login/')
def transition(request):
    user = request.user
    if user.status == 0:
        user.status = 1
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

        person = get_object_or_404(get_user_model(), id=request.user.id)
        followers = User.objects.all()
        for follower in followers:
            if follower in person.follower.all():
                if follower.status == 0 and follower.alarm == 1:
                    social_user = get_object_or_404(SocialAccount, id=follower.id-1)
                    send_notification(concert.musician.name, concert.date, concert.time, concert.address, social_user.extra_data['mobile']) 
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

@login_required(login_url='/accounts/naver/login/')
def alarm(request):
    user = request.user
    if user.alarm == 0:
        user.alarm = 1
        user.save()
    else:
        user.alarm = 0
        user.save()
    return redirect('mypage', user.id)

@login_required(login_url='/accounts/naver/login/')
def highlight(request, user_id):
    if request.method == "GET":
        person = get_object_or_404(get_user_model(), id=user_id)
        return render(request, "highlight_form.html", {'person': person})
    else:
        high = Highlight()
        high.uploader = request.user
        high.highlight = request.FILES.get('highlight')
        high.save()
        return redirect('mypage', user_id)

@login_required(login_url='/accounts/naver/login/')
def highlight_detail(request, high_id):
    high = get_object_or_404(Highlight, pk=high_id)
    return render(request, 'highlight_detail.html', {'high': high})

# 게시글 삭제 
@login_required(login_url='/accounts/naver/login/')
def delete_post(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    if request.method == 'GET':
        post.delete()
    return redirect('mypage', request.user.id)

# 게시글 수정
@login_required(login_url='/accounts/naver/login/')
def modify_post(request, post_id):
    post = get_object_or_404(Community, pk=post_id)
    if request.method == 'POST':
        post.author = request.user
        post.content = request.POST['content']
        post.created_at = timezone.now()
        try:
            #user.image = request.FILES['image']
            post.photo = request.FILES['photo']
            post.save()
        except:
            post.save()
        return redirect('mypage', request.user.id)

    else:
        return render(request, 'modify_post.html', {'post': post})

# 후기 삭제
@login_required(login_url='/accounts/naver/login/')
def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    if request.method == 'GET':
        feedback.delete()
    return redirect('mypage', request.user.id)
