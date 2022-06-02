from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account_app.models import User
from indie_app.models import Concert

# Create your views here.


@login_required(login_url='login')
def mypage_1(request):
    return render(request, 'mypage_1.html')

@login_required(login_url='login')
def mypage_2(request):
    return render(request, 'mypage_2.html')

@login_required(login_url='login')
def mypage_3(request):
    return render(request, 'mypage_3.html')

@login_required(login_url='login')
def musicpage_3(request):
    return render(request, 'musicpage_3.html')

@login_required(login_url='login')
def musicpage_2(request):
    return render(request, 'musicpage_2.html')

@login_required(login_url='login')
def musicpage_1(request):
    return render(request, 'musicpage_1.html')

# 공연 등록 창
def concert_form(request):
    return render(request, 'concert_form.html')

# 공연 등록 
def concert_create(request):
    if(request.method == 'POST'):
        concert = Concert() 
        concert.musician = request.user
        concert.introduce = request.POST['introduce'] 
        concert.date = request.POST['date']
        concert.time = request.POST['time']
        concert.latitude = request.POST['latitude']
        concert.longitude = request.POST['longitude']
        concert.save() 
    return redirect('home') 
