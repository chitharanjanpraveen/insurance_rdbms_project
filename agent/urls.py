from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url for agent management
    url(r'^$', views.home, name="home"),
    url(r'^auth/staff$', views.loginstaff, name="loginstaff"),
    url(r'^auth/user$', views.loginuser, name="loginuser"),
]
