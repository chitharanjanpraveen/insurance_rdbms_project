from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^logout$', views.logout, name="logout"),
]
