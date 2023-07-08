from django.db import models

class FileModel(models.Model):
    file = models.FileField(upload_to='pdf_files/')
    filename = models.CharField(max_length=255)

    def __str__(self):
        return self.filename
