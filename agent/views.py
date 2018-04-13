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
        request.session['agentname']=name;
        request.session['password'] =passa;
        request.session['name']=row2[0][1]
        return render(request, 'agent/agenthome.html', {'data':row2[0][1]})
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

def autoauth(request):
    name = request.session['agentname']
    passa = request.session['password']
    query = "SELECT * FROM agent_agent WHERE pass_word='" + passa + "' and agentid=" + name
    cursor2 = connection.cursor()
    cursor2.execute(query)
    row2 = cursor2.fetchall()
    count = len(row2)
    if count==1:
        return True;
    else:
        return False

def stafflogout(request):
    if autoauth(request):
        del request.session['agentname']
        del request.session['password']
        del request.session['name']
        return HttpResponseRedirect('/in')
    else:
        return HttpResponseRedirect('/in')

def changepass(request):
    if(autoauth(request)):
        oldpassword=str(request.POST.get("oldpass"))
        newpassword=str(request.POST.get("newpass"))
        conpassword=str(request.POST.get("conpass"))
        if(oldpassword!=request.session['password']):
            return render(request, 'agent/agenthome.html', {'data': request.session['name'], 'error':"Old password mismatch" })
        else:
            if newpassword==conpassword:
                query="UPDATE agent_agent SET pass_word='"+ conpassword +"'"
                cursor2 = connection.cursor()
                cursor2.execute(query)
                return render(request, 'agent/agenthome.html', {'data': request.session['name'], 'error':"Successfully changed your password"})
            else:
                return render(request, 'agent/agenthome.html', {'data': request.session['name'], 'error':"New password mismatch"})
    else:
        return HttpResponseRedirect('/in')

def addcus(request):
    if(autoauth(request)):
        return render(request, 'agent/addcus.html', {'data': request.session['name']})
    else:
        return HttpResponseRedirect('/in')