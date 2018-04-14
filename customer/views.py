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
    return render(request, 'customer/customerhome.html', {'data': "chitha"})


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




def customerlogout(request):
        if autoauth(request):
            del request.session['username']
            del request.session['passa']
            del request.session['name']
            return HttpResponseRedirect('/in')
        else:
            return HttpResponseRedirect('/in')

def addnominee(request):
    if(autoauth(request)):
        return render(request, 'customer/addnominee.html', {'data': request.session['cusname']})
    else:
        return HttpResponseRedirect('/in')
