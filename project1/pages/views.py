from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import InputForm

# Create your views here.

def sample(request):
    return HttpResponse("Welcome To Django")

#dynamic routing
def sample2(request,name):
    return HttpResponse(name)

#Trmplate_rendering
def sample3(request):
    return render(request,'index.html')

#context PAssing To Template
def sample4(request):
    ctx = {
        'name': 'Durjoy',
        'address': 'Klu'
    }
    return render(request, 'contextpass.html', ctx)

#list rendering
def sample5(request):
    lst={"lst":['a', 'b', 'c', 'd', 'e']}
    return render(request, 'listpass.html', lst)

#REDIRECT
def sample6(request):
    return redirect("lr")

#template Inheritence
def sample7(request):
    return render(request, "inheritance.html")

def sample8(request):
    return render(request, 'index2.html')


#Creating a user in admin panel
def registration(request):
    fname="ABC"
    lname="XYZ"
    email="abc@gmail.com"
    User.objects.create_user(fname,lname,email)
    return HttpResponse("Registration Successfull")

def sample9(request):
    return render(request,"index3.html")

def sample10(request):
    return render(request, "index4.html")

def onsubmit(request):
    fname=request.POST.get('fn')
    lname=request.POST.get('ln')
    mobile_no=request.POST.get('mn')
    print(fname)
    return HttpResponse(fname)

def sample11(request):
    context={}
    context['form']=InputForm()
    return render(request, "index5.html", context)