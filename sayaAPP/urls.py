from django.urls import path
from .views import *
from sayaAPP .views import *


urlpatterns = [
    path('base/', BaseView.as_view(), name='base'),
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('Donation/', DonationView.as_view(), name='donation'),
    path('donate/', DonateView.as_view(), name='donate'),
    path('mission/', MissionView.as_view(), name='mission'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('about/', AboutView.as_view(), name='about'),
    # path('post', PostListView.as_view(), name='post'),
    # # like and unlike partterns
    # path('post/<int:post_id>/like/', like_post, name='like_post'),
    # path('post/<int:post_id>/unlike/', unlike_post, name='unlike_post')
    
]


