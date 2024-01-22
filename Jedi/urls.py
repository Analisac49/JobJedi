from django.urls import path
from .views import job_application_list, job_application_detail, new_job_application, home, edit_job, delete_job, edit_notes, notes_view

urlpatterns = [
    path('', home, name='home'),
    path('applications/', job_application_list, name='job_application_list'),
    path('application/<int:pk>/', job_application_detail, name='job_application_detail'),
    path('new_application/', new_job_application, name='new_job_application'),
    path('edit-job/<int:job_application_id>/', edit_job, name='edit_job'),
    path('delete-job/<int:job_application_id>/', delete_job, name='delete_job'),
    path('edit-notes/<int:job_application_id>/', edit_notes, name='edit_notes'),
    path('notes/<int:job_application_id>/', notes_view, name='notes'),
]
