from django.contrib import admin
from.models import *

# Register your models here.

# userprofile
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_pic', 'website_url',
                    'facebook_url', 'twitter_url', 'instagram_url', 'youtube_url')
admin.site.register(UserProfile, UserProfileAdmin)



# contacted messages model

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message','phone_number')
admin.site.register(Contact, ContactAdmin)
# donation contact


class DonationContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone_number', 'created_at')
admin.site.register(DonationContact, DonationContactAdmin)

