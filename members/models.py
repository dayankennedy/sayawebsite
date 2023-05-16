from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User
# from django import forms

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True ,null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='/profile_pic/default_profile_pic.PNG/')
    website_url = models.CharField(max_length=50, null=True, blank=True)
    facebook_url = models.CharField(max_length=50, null=True, blank=True)
    twitter_url = models.CharField(max_length=50, null=True, blank=True)
    instagram_url = models.CharField(max_length=50, null=True, blank=True)
    youtube_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone= models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DonationContact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=4000)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)