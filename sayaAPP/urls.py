from django.urls import path
from .views import *


urlpatterns = [

    path('base/', BaseView.as_view(), name='base'),
    path('news/', AboutView.as_view(), name='about'),
    path('news/', ContactView.as_view(), name='contact'),
    path('news/', DonateView.as_view(), name='donate'),
    path('news/', MissionView.as_view(), name='mission'),
    path('news/', BlogListView.as_view(), name='news'),
    path('news/', PostListView.as_view(), name='post'),

    # # like and unlike partterns
    # path('post/<int:post_id>/like/', like_post, name='like_post'),
    # path('post/<int:post_id>/unlike/', unlike_post, name='unlike_post')
]


