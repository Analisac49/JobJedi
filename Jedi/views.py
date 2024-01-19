from django.shortcuts import render, get_object_or_404
from .models import JobApplication
from Jedi.forms import JobApplicationForm

def job_application_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'job_application_list.html', {'applications': applications})

def job_application_detail(request, pk):
    application = get_object_or_404(JobApplication, pk=pk)
    return render(request, 'job_application_detail.html', {'application': application})

def new_job_application(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = JobApplicationForm()

    return render(request, 'new_job_application.html', {'form': form})
