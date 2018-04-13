from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^auth/staff$', views.loginstaff, name="loginstaff"),
    url(r'^auth/user$', views.loginuser, name="loginuser"),
    url(r'^staff/logout$', views.stafflogout, name="stafflogout"),
    url(r'^staff/pass$', views.changepass, name="changepass"),
    url(r'^staff/add$', views.addcus, name="addcus"),
]
