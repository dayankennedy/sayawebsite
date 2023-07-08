from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]
