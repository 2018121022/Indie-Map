from django.shortcuts import render
from account_app.models import Concert
from datetime import date # import 필요 


def map(request):
    # dateField가 오늘 날짜인 공연만 전송 
    concerts = Concert.objects.filter(date__range=[date.today(), date.today()]).values().all()    
    return render(request, 'map.html', {'concerts': concerts})

def login_map(request):
    concerts = Concert.objects.filter(date__range=[date.today(), date.today()]).values().all()
    return render(request, 'login_map.html', {'concerts': concerts})

def each_map(request):
    return render(request, 'each_map.html')

