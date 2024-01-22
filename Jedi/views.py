from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from .forms import JobApplicationForm, NotesForm

@login_required
def home(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'job_application_list.html', {'applications': applications})

@login_required
def job_application_list(request):
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'job_application_list.html', {'applications': applications})

@login_required
def job_application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk, user=request.user)
    return render(request, 'job_detail.html', {'application': application})

@login_required
def new_job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.save()
            return redirect('job_application_list')
    else:
        form = JobApplicationForm()

    return render(request, 'new_job.html', {'form': form})

@login_required
def edit_job(request, job_application_id):
    job_application = get_object_or_404(JobApplication, id=job_application_id, user=request.user)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job_application)
        if form.is_valid():
            form.save()
            return redirect('job_application_detail', pk=job_application_id)
    else:
        form = JobApplicationForm(instance=job_application)

    return render(request, 'edit_job.html', {'form': form, 'job_application': job_application})

@login_required
def delete_job(request, job_application_id):
    job_application = get_object_or_404(JobApplication, id=job_application_id, user=request.user)

    if request.method == 'POST':
        job_application.delete()
        return redirect('job_application_list')

    return render(request, 'delete_job.html', {'job_application': job_application})

@login_required
def edit_notes(request, job_application_id):
    application = get_object_or_404(JobApplication, id=job_application_id, user=request.user)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('job_application_detail', pk=job_application_id)
    else:
        form = NotesForm(instance=application)

    return render(request, 'edit_notes.html', {'application': application, 'form': form})

@login_required
def notes_view(request, job_application_id):
    application = get_object_or_404(JobApplication, id=job_application_id, user=request.user)
    form = NotesForm(instance=application)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('job_application_detail', pk=job_application_id)

    return render(request, 'edit_notes.html', {'application': application, 'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')
