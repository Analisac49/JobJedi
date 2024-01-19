from django.db import models
from django.contrib.auth.models import User

# Model for representing a Job Application
class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    date_applied = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.position} at {self.company} ({self.user.username})"

# Model for representing Notes associated with a Job Application
class Note(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.job_application.position} ({self.job_application.user.username})"