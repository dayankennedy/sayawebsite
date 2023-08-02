from django.contrib import admin
from .models import *


# changing the headers on the website

admin.site.site_header = 'SRDO Admin'
admin.site.site_title = 'SRDO ADMIN'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image')
    list_filter = ('title',)
    list_display_links = ['title', 'date']
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)


# comments registration
class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text', 'date')
    list_display_links = ['author',]
    search_fields = ('author', 'text')


admin.site.register(CommentPost, CommentPostAdmin)


# comments post
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'phone', 'date')
    list_display_links = ['name', 'email']
    search_fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)


# donations registration
class DonationContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'phone', 'date')
    list_display_links = ['name', 'email']
    search_fields = ('name', 'email')


admin.site.register(DonationContact, DonationContactAdmin)


# likes comments
admin.site.register(LikePost)

# admin.site.register(Category)
