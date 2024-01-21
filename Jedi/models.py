from django.db import models
from django.contrib.auth.models import User

# Model for representing a Job Application
class JobApplication(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date_applied = models.DateField()
    status = models.CharField(max_length=20)
    job_description = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='jedi_job_applications'
    )

    def __str__(self):
        return f"{self.position} at {self.company} - {self.user.username if self.user else 'No User'}"

# Model for representing Notes associated with a Job Application
class Note(models.Model):
    job_application = models.ForeignKey(
        JobApplication, 
        on_delete=models.CASCADE, 
        related_name='jedi_notes'
    )
    
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.job_application.position} ({self.job_application.user.username if self.job_application.user else 'No User'})"
