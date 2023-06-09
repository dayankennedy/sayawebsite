from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView,CreateView, TemplateView
from django.views.generic import DeleteView, UpdateView
from django.views.generic import DetailView
from .models import *
from crequest.middleware import CrequestMiddleware
# Create your views here.

class BaseView(TemplateView):
    template_name='sayaAPP/Base.html'

# about view
class AboutView(TemplateView):
    template_name='sayaAPP/about.html'


# conact view
def contact(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        phone = request.POST.get('phone')
        form.name = name
        form.email = email
        form.massage = massage
        form.phone = phone
        form.save()
    else:
        return render(request, 'sayaAPP/contact.html')

# donation view
class DonateView(TemplateView):
    template_name='sayaAPP/donate.html'

# mission view
class MissionView(TemplateView):
    template_name='sayaAPP/mission.html'

# bolog view
class BlogListView(ListView):
    model = Post
    template_name='sayaAPP/blogPage.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']

# home view
class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='sayaAPP/home.html'
    paginate_by = 2
    ordering = ['-pub_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = context['object_list']
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

# donation view
class DonationView(TemplateView):

    template_name='sayaApp/donation.html'
