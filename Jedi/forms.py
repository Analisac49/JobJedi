from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['position', 'company', 'date_applied', 'status', 'job_description', 'notes']

class NotesForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['notes']