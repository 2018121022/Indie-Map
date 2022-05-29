from django.shortcuts import render

# Create your views here.

def map(request):
    return render(request, 'map.html')

def login_map(request):
    return render(request, 'login_map.html')

def each_map(request):
    return render(request, 'each_map.html')