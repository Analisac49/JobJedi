from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import JobApplication
from .forms import LoginForm

def job_application_list(request):
    job_applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'job_application_list.html', {'job_applications': job_applications})

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()

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

def new_job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.save()
            messages.success(request, 'Job application submitted successfully.')
            return redirect('job_application_list')
    else:
        form = JobApplicationForm()

    return render(request, 'new_job_application.html', {'form': form})
