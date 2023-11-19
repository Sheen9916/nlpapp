# urls.py
from django.urls import path
from .views import upload_job_posting

urlpatterns = [
    path('', upload_job_posting, name='upload_job_posting'),
    # Add other URLs as needed
]
