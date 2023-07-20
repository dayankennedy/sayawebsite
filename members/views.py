from django.views.generic import TemplateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import createUserForm
from django.contrib import messages
from .models import *
from sayaAPP.models import *


# from .forms import ContactForm
app_name = 'members'

# Create your views here.
def thanks(request):
    return render(request, 'members/thanks.html')


# signup view
def signup(request):
    form = createUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,  'account created for ' + user)
            return redirect('login')
    else:
        form = createUserForm()
    return render(request, 'members/signup.html', {'form': form})




# login function
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog')
        else:
            messages.info(request, 'username OR password is incorrect')
            return redirect("login")
    return render(request, 'members/loginPage.html')


# logout views
def logoutPage(request):
    logout(request)
    return redirect('home')

# # profile update views
class UserEditView(UpdateView):
    template_name = 'edit_profile.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user

# user profile 
class UserProfileView(TemplateView):
    model = UserProfile
    template_name = 'user_profile.html'
    fields = '__all__'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user

# this thanks page

