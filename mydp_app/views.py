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

@login_required(login_url='login')
def createBanner(request):
    form = BannerForm
    slug_field = 'slug'
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        banner = Banner.objects.create(
            user = request.user,
            banner_name = request.POST.get('banner_name'),
            description = request.POST.get('description'),
            slug = request.POST.get('slug'),
            category = request.POST.get('category_name'),
            tag = request.POST.get('tag_name'),
            banner_image = request.POST.get('banner_image'),
        )
        return redirect('home')
    context = {'form':form, 'categories':categories, 'tags':tags}
    return render(request, 'create-banner.html', context)

@login_required(login_url='login')
def userBanner(request):
    form = UserBannerForm
    if request.method == 'POST':
        form = UserBannerForm()
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occured during banner creation')
    context = {'form':form}
    return render(request, 'create-banner.html', context)

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
