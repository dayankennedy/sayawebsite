from django.contrib import admin
from .models import *


# changing the headers on the website 

admin.site.site_header = 'SRDO Admin'
admin.site.site_title='SRDO ADMIN'

class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'pub_date', 'image')
admin.site.register(Post,PostAdmin)


# comments registration
admin.site.register(CommentPost)


# likes comments
admin.site.register(LikePost)
admin.site.register(Contact)