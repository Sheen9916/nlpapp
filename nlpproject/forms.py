# forms.py
from django import forms

class JobPostingForm(forms.Form):
    document = forms.FileField()
