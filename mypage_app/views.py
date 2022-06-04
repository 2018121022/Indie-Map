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

