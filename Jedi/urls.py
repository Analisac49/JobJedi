from django.urls import path
from .views import job_application_list, job_application_detail, new_job_application, home

urlpatterns = [
    path('', job_application_list, name='home'),
    path('applications/', job_application_list, name='job_application_list'),
    path('application/<int:pk>/', job_application_detail, name='job_application_detail'),
    path('new_application/', new_job_application, name='new_job_application'),
    path('', home, name='home'),
]
