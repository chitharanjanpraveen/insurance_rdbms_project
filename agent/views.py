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
            return render(request, 'agent/changepass.html', {'data': request.session['name'], 'error':"Old password mismatch" })
        else:
            if newpassword==conpassword:
                query="UPDATE agent_agent SET pass_word='"+ conpassword +"' WHERE agentid=" + str(request.session['agentname'])
                cursor2 = connection.cursor()
                cursor2.execute(query)
                request.session['password']=conpassword
                return render(request, 'agent/changepass.html', {'data': request.session['name'], 'error':"Successfully changed your password"})
            else:
                return render(request, 'agent/changepass.html', {'data': request.session['name'], 'error':"New password mismatch"})
    else:
        return HttpResponseRedirect('/in')

def addcus(request):
    if(autoauth(request)):
        return render(request, 'agent/addcus.html', {'data': request.session['name']})
    else:
        return HttpResponseRedirect('/in')

def changepassword(request):
    if autoauth(request):
        return render(request, 'agent/changepass.html', {'data': request.session['name']})
    else:
        return HttpResponseRedirect('/in')

def addtodb(request):
    if autoauth(request):
        newagent = customer()
        newagent.Fname=str(request.POST.get('first_name'))
        newagent.Lname=str(request.POST.get('second_name'))
        newagent.phone_no=str(request.POST.get('phone'))
        newagent.email=str(request.POST.get('email'))
        newagent.pass_word=str(request.POST.get('passa'))
        newagent.age=str(request.POST.get('age'))
        newagent.DOB=str(request.POST.get('dob'))
        newagent.address=str(request.POST.get('per_add'))
        newagent.sex=str(request.POST.get('gender'))
        newagent.Cagent_id= agent.objects.only('agentid').get(agentid=request.session['agentname'])
        newagent.save()
        return render(request, 'agent/agenthome.html', {'data': request.session['name'], 'error':newagent.cust_id})
    else:
        return HttpResponseRedirect('/in')

def transaction(request):
    if autoauth(request):
        return render(request, 'agent/tran.html', {'data': request.session['name']})
    else:
        return HttpResponseRedirect('/in')

def viewtrans(request):
    if autoauth(request):
        name=str(request.POST.get('custid'))
        query="SELECT policyno,payment_num,payment_amount,payment_date FROM customer_payment,customer_customer,customer_policy WHERE"
    else:
        return HttpResponseRedirect('/in')

def update(request):
    if autoauth(request):
        return render(request, 'agent/update.html', {'data': request.session['name']})
    else:
        return HttpResponseRedirect('/in')


def updatedone(request):
    if autoauth(request):
        query="SELECT * FROM customer_customer WHERE cust_id=" + str(request.POST.get('id'))
        cursor2 = connection.cursor()
        cursor2.execute(query)
        row2 = cursor2.fetchall()
        return render(request, 'agent/updatepage.html', {'data':request.session['name'], 'logdata':row2})
    else:
        return HttpResponseRedirect('/in')

def updatedonetodb(request):
    if autoauth(request):
        newagent = customer.objects.get(cust_id=int(request.POST.get('cusid')))
        newagent.phone_no=str(request.POST.get('phone'))
        newagent.email=str(request.POST.get('email'))
        newagent.age=str(request.POST.get('age'))
        newagent.DOB=str(request.POST.get('dob'))
        newagent.address=str(request.POST.get('per_add'))
        newagent.sex=str(request.POST.get('gender'))
        newagent.save()
        return render(request, 'agent/agenthome.html', {'data': request.session['name'], 'error':newagent.cust_id})
    else:
        return HttpResponseRedirect('/in')