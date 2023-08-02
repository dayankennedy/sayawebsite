from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic import DeleteView, UpdateView
from django.views.generic import DetailView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BaseView(TemplateView):
    template_name = 'sayaAPP/Base.html'

# home view


class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'sayaAPP/home.html'
    paginate_by = 2
    ordering = ['-date']

# about view


class AboutView(TemplateView):
    template_name = 'sayaAPP/about.html'


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
    template_name = 'sayaAPP/donate.html'


# mission view
class MissionView(TemplateView):
    template_name = 'sayaAPP/mission.html'


# blog view
class BlogListView(ListView):
    model = Post
    template_name = 'sayaAPP/blogPage.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 2


# post detail view
class BlogdetailsView(DetailView, LoginRequiredMixin):
    model = Post
    context_object_name = 'posts'
    template_name = 'sayaApp/postdetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = self.object.image
        context['title'] = self.object.title
        return context

# donation view


class DonationView(TemplateView):
    template_name = 'sayaApp/donation.html'


class UpdateDetailview(UpdateView):
    model = Post
    fields = ['title', 'content']
    context_object_name = 'posts'
    template_name = 'sayaApp/post_update.html'


class postDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    context_object_name = 'post'
    template_name = 'sayaApp/post_delete.html'


class postCreateView(CreateView):
    model = Post
    context_object_name = 'posts'
    template_name = 'sayaApp/create_post.html'


def like_post(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    post.save()

    # return redirect(request.META['HTTP_REFERER'])
