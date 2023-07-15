from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User



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