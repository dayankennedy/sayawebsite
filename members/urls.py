from .views import UserEditView, UserProfileView
from django.urls import path
from .import views
from sayaAPP.views import *
urlpatterns = [
    path('', views.signup, name='signup'),
    path('thanks/', views.thanks, name='thanks'),
    path('loginPage/', views.loginPage, name='login'),
    path('logoutPage/', views.logoutPage, name='logout'),
    path('edit_profile/<int:slug>',  UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:slug>', UserProfileView.as_view(), name='profile'),
]
