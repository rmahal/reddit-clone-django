from django.shortcuts import render, redirect
from reddit.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
import datetime

def index(request):
    postsToShow = Post.objects.all()

    if request.method == 'POST':
        timestamp = "100"
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        picture = request.POST.get('picture')
        vote_total = 0
        site_url = request.POST.get('site_url')
        post_form = PostForm(data=request.POST)
        #print("\n\n"+post_form+"\n\n")
        if post_form.is_valid():
            post = post_form
            post.save()
        else:
            print(post_form.errors)
    else:
        post_form = PostForm()
    
    return render(request,'reddit/index.html', {'post_form': post_form, 'posts': postsToShow})


@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'reddit/registration.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'reddit/login.html', {})