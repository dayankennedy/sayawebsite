from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView,CreateView, TemplateView
from django.views.generic import DeleteView, UpdateView
from .models import *
# Create your views here.


class BaseView(TemplateView):
    template_name='sayaAPP/Base.html'


class AboutView(TemplateView):
    template_name='sayaAPP/about.html'


class ContactView(TemplateView):

    template_name='sayaAPP/contact.html'


class DonateView(TemplateView):
    template_name='sayaAPP/donate.html'


class MissionView(TemplateView):
    template_name='sayaAPP/misson.html'


class BlogListView(ListView):
    model = Post
    template_name='sayaAPP/blogPage.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']

class HomeView(TemplateView):
    template_name='sayaAPP/home.html'



