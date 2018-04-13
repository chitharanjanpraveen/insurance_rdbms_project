from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #urls to manage agent
    url(r'^$', views.home, name="home"),
    url(r'^auth/staff$', views.loginstaff, name="loginstaff"),
    url(r'^auth/user$', views.loginuser, name="loginuser"),
]
