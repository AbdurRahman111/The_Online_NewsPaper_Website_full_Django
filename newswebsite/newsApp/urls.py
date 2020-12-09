from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # this is for posting comments
    path('postComments', views.postComments, name='postComments'),
    path('login', views.login_finc, name='login'),
    path('logout', views.logout_func, name='logout'),
    path('signup', views.signup, name='signup'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),

    #this is for like
    path('like/', views.LikeView, name= 'like_post'),


    # API to post comments
    path('', views.index, name='index'),
    path('<str:slug>', views.blogPost, name='blogPost'),



]

