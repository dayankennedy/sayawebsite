
from django.shortcuts import render
from django.http import FileResponse
import os
from .models import *

# creating the download view

def download(request):
    # Replace 'path_to_pdf' with the actual path to your PDF file
    path_to_pdf = 'Media/media/pdf_files/sabot_final.pdf'
    filename = os.path.basename(path_to_pdf)
    with open(path_to_pdf, 'rb') as pdf_file:
        response = FileResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

