from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
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
    posts = Post.objects.all()
    context = {'posts': posts}
    posts = Post.objects.order_by('- pub_date')
    return render(request, 'sayaAPP/news.html',context)



@login_required
def like_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    LikePost.objects.create(user=request.user, post=post)
    return redirect('post_detail', post_id=post.id)

# 

@login_required
def unlike_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    LikePost.objects.filter(user=request.user, post=post).delete()
    return redirect('post_detail', post_id=post.id)
