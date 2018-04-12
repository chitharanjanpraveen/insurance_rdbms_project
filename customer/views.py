from .models import *
from agent.models import *
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import connection
from datetime import datetime

# Create your views here.

def home(request):
    if(autoauth(request)):
        return HttpResponse('<a href="/cust/logout">Logout</a>')
    else:
        return HttpResponseRedirect('/in/')


def autoauth(request):
    name = str(request.session["username"])
    passa = str(request.session["passa"])
    query = "SELECT * FROM customer_customer WHERE pass_word='" + passa + "' and cust_id=" + name
    cursor2 = connection.cursor()
    cursor2.execute(query)
    row2 = cursor2.fetchall()
    count = len(row2)
    if count==1 :
        return True
    else:
        return False

def logout(request):
    del request.session["username"]
    del request.session["passa"]
    return HttpResponseRedirect('/in')
