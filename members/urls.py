from .views import UserEditView, UserProfileView
from django.urls import path
from.import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('loginPage/', views.loginPage, name='login'),
    path('logoutPage/', views.logoutPage, name='logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),

]
