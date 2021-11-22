from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def loginPage(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
             
    return render(request,'registration/login.html', context)

def registerPage(request):
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'registration/register.html', {'form':form})

def logoutPage(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'home.html')

# @login_required(login_url='login')


@login_required(login_url='login')
def createBanner(request):
    form = BannerForm
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            banner = form.save(commit=False)
            banner.user = request.user
            banner.save()
            return redirect('home')
    return render(request, 'create-banner.html', {'form':form})


def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    banners = user.banner_set.all()
    form = UserProfileForm(
        initial={
            'username':user.username,
            'full_name':user.full_name,
            'avatar':user.avatar,
        }
        ) 
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance = request.user) 
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            return redirect('user-profile', username)

    context = {'user':user, 'banners':banners, 'form':form}
    return render(request, 'user-profile.html', context)


def deleteAccount(request):
    user = request.user
    user.delete()
    return redirect('home')


def viewBanner(request, slug):
    banner = Banner.objects.get(slug=slug)
    comment = Comment.objects.filter(banner=banner)
    form = CommentForm
    context = {'banner': banner, 'comment':comment, 'form':form}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            banner = form.save(commit=False)
            banner.user = request.user
            banner.banner = banner
            banner.save()
            return redirect('view-banner', slug)
    return render(request, 'view-banner.html', context)

@login_required(login_url='login')
def useBanner(request, slug):
    banner = Banner.objects.get(slug=slug)
    form = UserBannerForm
    if request.method == "POST":
        form = UserBannerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'user-profile', user.username)
    return render(request, 'use-banner.html', {'form':form})

def allBannerCategory(request):
    allBannerCategory= Category.objects.all()
    context = {'allBannerCategory': allbannerCategory}
    return render(request, 'all-banner-category', context)

def bannerCategory(request, category_name):
    category = Category.objects.get(category_name)
    bannerCategory = Banner.objects.filter(category)
    context = {'bannerCategory':bannerCategory}
    return render(request, 'banner-category', context)

# def discoverPage(request):
#     banners = Banner.objects.filter