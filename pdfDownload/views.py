
from django.shortcuts import render,redirect
from django.http import HttpResponse, FileResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
from .models import *

# creating the download view
def download(request):
    # Retrieve the file object from the database or any other source
    file_obj = get_object_or_404(FileModel)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_obj.file))
    # Open the file using FileResponse
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="' + file_obj.filename + '"'

    
    return render(request,'pdfDownload/download.html')
