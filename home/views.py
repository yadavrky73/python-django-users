from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')                     # changed from 'index'
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('/')                 # changed from 'index'
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('login')                     # this is fine, 'login' exists