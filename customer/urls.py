from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^logout$', views.customerlogout, name="customerlogout"),
    url(r'^add$', views.addnominee, name="addnominee"),
    url(r'^update$', views.update, name="update"),

]
