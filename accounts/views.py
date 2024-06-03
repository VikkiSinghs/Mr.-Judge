from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# to register a new user
def register_user(request):

    if request.method == 'POST':
        # extract username and password
        username = request.POST.get('username')
        password = request.POST.get('password')
        # if username exists return the username passed throught the post method
        user = User.objects.filter(username=username)
        # return a message & redirect
        if user.exists():
            messages.info(request,'User with this username already exists')
            return redirect("/auth/register/")
        # if user dosen't exist
        user = User.objects.create_user(username=username)
        # add seperately to be able to encrypt password
        user.set_password(password)

        user.save()
        # return message and redirect to registe page
        messages.info(request,'User created successfully')
        return redirect('/auth/register/')
    # if user visiting for the first time, redirect to
    template = loader.get_template('register.html')
    context = {}
    return HttpResponse(template.render(context,request))
    
# for user login    
def login_user(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check username dosen't exists, return a message and redirect to login
        if not User.objects.filter(username=username).exists():
            messages.info(request,'User with this username does not exist')
            return redirect('/auth/login/')
        # if user exists, then authenticate the user
        user = authenticate(username=username, password=password)
        # for invalid password
        if user is None:
            messages.info(request,'invalid password')
            return redirect('/auth/login')
        
        # for an authenticated user - LOGIN and redirct
        login(request,user)
        messages.info(request,'login successful')
        # location for all questions
        return redirect('/home/qus/')
    # if request.method != 'POST' then user might've just arrived to login page
    template = loader.get_template('login.html')
    context ={}
    return HttpResponse(template.render(context,request))


def logout_user(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('/auth/login/')