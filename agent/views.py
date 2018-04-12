from .models import agent, office
from customer.models import *
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db import connection
from datetime import datetime

app_name = 'agent'

#admin functions here

def home(request):
    return render(request, 'agent/home.html', {'data':"ravi"})

def loginstaff(request):
    name = str(request.POST.get("username"))
    passa = str(request.POST.get("passa"))
    query = "SELECT * FROM agent_agent WHERE pass_word='" + passa + "' and agentid=" + name
    cursor2 = connection.cursor()
    cursor2.execute(query)
    row2 = cursor2.fetchall()
    count = len(row2)
    if count==1 :
        return HttpResponse("<h1>Success fully logged in</h1>")
    else:
        return HttpResponseRedirect('/in/')

def loginuser(request):
    name = str(request.POST.get("username"))
    passa = str(request.POST.get("passa"))
    query = "SELECT * FROM customer_customer WHERE pass_word='" + passa + "' and cust_id=" + name
    cursor2 = connection.cursor()
    cursor2.execute(query)
    row2 = cursor2.fetchall()
    count = len(row2)
    if count==1 :
        request.session["username"]=name;
        request.session["passa"] = passa;
        return HttpResponseRedirect('/cust/')
    else:
        return HttpResponseRedirect('/in/')

