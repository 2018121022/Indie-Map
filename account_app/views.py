from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
        return redirect('home')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    errMsg = {}
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
            user.save()
            login(request, user)
            return redirect("home")
        else:
            errMsg = "Passwords do not match. Please check it again."
            return render(request, 'signup.html', {'error': errMsg})
    else:
        return render(request, 'signup.html')

def account(request):
    return render(request, 'account.html')