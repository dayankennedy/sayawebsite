from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.donate, name='donate'),
    path('contact/', views.mission, name='mission'),
    path('contact/', views.contact, name='contact'),
]
