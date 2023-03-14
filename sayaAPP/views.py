from django.shortcuts import render
from .models import *
# Create your views here.


def base(request):
    return render(request, 'sayaAPP/base.html')

def home(request):
    return render(request, 'sayaAPP/home.html')

def about(request):
    return render(request, 'sayaAPP/about.html')

def contact(request):
    return render(request, 'sayaAPP/contact.html')

def donate(request):

    return render(request, 'sayaAPP/donate.html')

def mission(request):
    return render(request, 'sayaAPP/mission.html')


def news(request):

    return render(request, 'sayaAPP/news.html')
