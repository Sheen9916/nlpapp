
# Create your views here.
from django.shortcuts import render, redirect
from .forms import JobPostingForm
from.models import JobPosting
from django.http import HttpResponse
import spacy


def extract_job_details(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

def upload_job_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST, request.FILES)
        if form.is_valid():
            document = request.FILES['document'].read().decode('latin-1')
            job_details = extract_job_details(document)
            # Create a JobPosting instance and save it to the database
            JobPosting.objects.create(**job_details)
            return redirect('success_page')
    else:
        form = JobPostingForm()
        print("formm.....")

    return render(request, 'upload_job_posting.html', {'form': form})


# def upload_job_posting(request):
#     if request.method == 'POST':
#         form = JobPostingForm(request.POST, request.FILES)
#         if form.is_valid():
#             document = request.FILES['document'].read().decode('latin-1')
#             job_details = extract_job_details(document)
            
#             # Create a JobPosting instance and save it to the database if job details are available
#             if job_details:
#                 JobPosting.objects.create(
#                     title=job_details['title'],
#                     company=job_details['company'],
#                     description=job_details['description'],
#                     requirements=job_details['requirements']
#                 )
#                 return redirect('success_page')
#     else:
#         form = JobPostingForm()
#         print("formm.....")

#     return render(request, 'upload_job_posting.html', {'form': form})








# def upload_job_posting(request):
#     if request.method == 'POST':
#         form = JobPostingForm(request.POST, request.FILES)
#         if form.is_valid():
#             document = request.FILES['document'].read().decode('latin-1')
#             job_details = extract_job_details(document)
            
#             if job_details:  # Check if job_details is not None or empty
#                 JobPosting.objects.create(**job_details)
#                 return redirect('success_page')
#             else:
#                 # Handle case where job_details is None or empty
#                 return HttpResponse("Failed to extract job details")
#     else:
#         form = JobPostingForm()
#         print("formm.....")

#     return render(request, 'upload_job_posting.html', {'form': form})




# def extract_job_details_from_pdf(file_content):
#     try:
#         pdf_reader = PdfReader(BytesIO(file_content))
#         # Process PDF content to extract job details
#         # Implement logic to extract job details from the PDF
#         job_details = {
#             'title': 'Extracted Title',
#             'description': 'Extracted Description',
#             # Add other extracted job details
#         }
#         return job_details
#     except Exception as e:
#         print(f"Error extracting job details from PDF: {e}")
#         return {}  # Return an empty dictionary on error

# def upload_job_posting(request):
#     if request.method == 'POST':
#         form = JobPostingForm(request.POST, request.FILES)
#         if form.is_valid():
#             pdf_file = request.FILES['document'].read()
#             job_details = extract_job_details_from_pdf(pdf_file)
            
#             if job_details:
#                 JobPosting.objects.create(**job_details)
#                 return redirect('success_page')
#             else:
#                 return HttpResponse("Failed to extract job details from the PDF")
#     else:
#         form = JobPostingForm()
#         print("formm.....")

#     return render(request, 'upload_job_posting.html', {'form': form})




