from django.urls import path
from .import views

urlpatterns = [
    # Other URL patterns for pdf view
    path('download/', views.download, name='download_file'),
    
]
