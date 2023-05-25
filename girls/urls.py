from django.urls import path
from .views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from girls import views as girls_views

urlpatterns = [
    #path('', views.post_list, name='post_list'),
    path('',post_list),
    path('post/<int:pk>/',post_detail, name='post_detail'),
    path('post/new/',post_new, name='post_new'),
    path('post/<int:pk>/edit/',post_edit, name='post_edit'),
    path('register/',register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='girls/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='girls/logout.html'), name='logout'),
    path('profile/', girls_views.profile, name='profile'),
    path('search/', search, name='search'),
]