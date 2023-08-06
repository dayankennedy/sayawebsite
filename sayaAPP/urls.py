from django.urls import path
from sayaAPP.views import *  # generic views
from .import views

urlpatterns = [
    path('base/', BaseView.as_view(), name='base'),
    path('', HomeView.as_view(), name='home'),
    path('Donation/', DonationView.as_view(), name='donation'),
    path('donate/', DonateView.as_view(), name='donate'),
    path('mission/', MissionView.as_view(), name='mission'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', views.contact, name='contact'),
    # generic classe base views
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>',BlogdetailsView.as_view() , name='postdetail'),
    path('updatedetail/<int:pk>',UpdateDetailview.as_view() , name='postupdate'),
    path('postdelete/<int:pk>',postDelete.as_view() , name='postdelete'),
    # # like and unlike partterns
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    # path('post/<int:post_id>/unlike/', unlike_post, name='unlike_post')
]

