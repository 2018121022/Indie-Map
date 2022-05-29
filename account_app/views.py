from django.shortcuts import render

# Create your views here.

def account(request):
    return render(request, 'account.html')

def callback(requset):
    return render(requset,'callback.html')