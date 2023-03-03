from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def signup(request):
    if(request.method=='POST'):
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['password1']
        password2=request.POST['password2']
        if(password==password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username Already Exists ⚠')
                return redirect('/signup/')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email Already Exists ⚠')
                return redirect('/signup/')
            else:
                 user=User.objects.create_user(username=username,email=email,password=password)
                 user.save();
                 print('User created')
        else:
            messages.info(request,'Password mismatched ⚠')
            return redirect('/signup/')
        return redirect('/Login/')
    else:
        return render(request,'firstapp/signup.html')
def login(request):
    if(request.method=='POST'):
        username=request.POST['uname']
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials ⚠')
            return redirect('/Login/')
    else:
        return render(request,'firstapp/Login.html')
def home(request):
    return render(request,'firstapp/Login.html')