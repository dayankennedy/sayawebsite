from django.contrib import admin
from.models import *

# Register your models here.

# userprofile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_pic', 'website_url',
                    'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')
admin.site.register(UserProfile, UserProfileAdmin)

