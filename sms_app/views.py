from django.shortcuts import render

# Create your views here.

def sms(request):
    return render(request, 'sms.html')