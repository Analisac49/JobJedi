from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered. Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
