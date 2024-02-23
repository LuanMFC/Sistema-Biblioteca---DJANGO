from django.contrib.auth import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    else:
        user = AuthenticationForm()
    return render(
        request, 
        "login.html",
        {"user": user}
    )

def SingIn(request):
    if request.method == "POST":
        user = UserCreationForm(request.POST)

        if user.is_valid():
            user.save()
            return redirect('list')
        
    else:
        user = UserCreationForm()
    return render(request,'singin.html', {'userForm': user})

def Logout(request):
    logout(request)
    return redirect('list')

