from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
from hitcount.views import HitCountDetailView
from datetime import datetime, timedelta

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


@login_required(login_url='login')
def createBanner(request):
    form = BannerForm
    slug_field = 'slug'
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            banner = form.save(commit=False)
            banner.user = request.user
            banner.slug = banner.slug
            banner.save()
            return redirect('view-banner', slug=banner.slug)
    context = {'form':form, 'categories':categories, 'tags':tags}
    return render(request, 'create-banner.html', context)

@login_required(login_url='login')
def editBanner(request, slug):
    banner = get_object_or_404(Banner.objects.all(), slug=slug)
    if request.user == banner.user:
        form = BannerForm(instance = banner)
        if request.method =="POST":
            form = BannerForm(request.POST, request.FILES, instance = banner)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form':form, 'banner':banner}
        return render(request, 'edit-banner.html', context)
    return redirect('home')
    

@login_required(login_url='login')
def deleteBanner(request, slug):
    banner = Banner.objects.get(slug = slug)
    if banner.user == request.user:
        banner.delete()
        return redirect('home')
    return redirect('home')

def userProfile(request, username):
    user = get_object_or_404(User, username=username)
    banners = user.banner_set.all()
    form = UserProfileForm(instance= user) 
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance = user) 
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

def Categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)

def home(request):
    banners = Banner.objects.all()
    comment = Comment.objects.all()
    context = {'banners':banners, 'comment':comment}
    return render(request, 'home.html', context)

class viewBanner(HitCountDetailView):
    model = Banner
    template_name = 'view-banner.html'
    context_object_name = 'banner'
    count_hit = True
    slug_field = 'slug'
    ordering = ['-created']
    def get_context_data(self, **kwargs):
        context = super(viewBanner, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(banner=self.object)
        context['comments_count'] = context['comments'].count()
        context['banner_users'] = self.object.banner_users.all()[:5]
        context['form'] = CommentForm()
        context['usebannerform'] = UserBannerForm()
        context['deletecommentform'] = CommentForm()
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = CommentForm(request.POST)
        usebannerform = UserBannerForm(request.POST, request.FILES)
        deletecommentform = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.banner = self.object
            comment.save()
            return redirect('view-banner', slug=self.object.slug)
        if usebannerform.is_valid():
            usebanner = usebannerform.save(commit=False)
            usebanner.user = request.user
            usebanner.banner = self.object
            usebanner.save()
            self.object.banner_users.add(request.user)
            return redirect('preview-banner', slug=self.object.slug)
        if deletecommentform.is_valid():
            comment = deletecommentform.save(commit=False)
            comment.user = request.user
            comment.banner = self.object
            comment.save()
            return redirect('view-banner', slug=self.object.slug)
        return self.render_to_response(context)

@login_required(login_url='login')
def usebanner(request, slug):
    banner = get_object_or_404(Banner.objects.all(), slug=slug)
    form = UserBannerForm(request.POST, request.FILES)
    if form.is_valid():
        usebanner = form.save(commit=False)
        usebanner.user = request.user
        usebanner.banner = banner
        usebanner.save()
        banner.banner_users.add(request.user)
        return redirect('preview-banner', slug=banner.slug)
    return redirect('home')

@login_required(login_url='login')
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('view-banner', slug=comment.banner.slug)

def bannerCategory(request, category_name):
    category = Category.objects.get(name=category_name)
    banners = Banner.objects.filter(category=category)
    context = {'banners':banners, 'category':category}
    return render(request, 'banner-category.html', context)

def previewBanner(request, slug):
    banner = Banner.objects.get(slug=slug)
    userbanner = UserBanner.objects.get(banner=banner)
    context = {'banner':banner, 'userbanner':userbanner}
    return render(request, 'preview-banner.html', context)


def discoverPage(request):
    context = {}
    a_month_ago = datetime.today() - timedelta(days=31)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    searchbar_word = request.GET.get('q')
    banners = Banner.objects.filter(
        Q(name__icontains=q) | 
        Q(user__username__icontains=q) |
        Q(user__full_name__icontains=q) |
        Q(description__icontains=q) 
    )
    most_viewed = Banner.objects.filter(created__gte = a_month_ago).order_by('-hit_count_generic__hits')[:6]
    most_used = Banner.objects.filter(created__gte = a_month_ago).order_by('banner_users')[:6]
    all_most_viewed_banner = Banner.objects.order_by('-hit_count_generic__hits')[:6]
    all_most_used_banner = Banner.objects.order_by('banner_users')[:6]
    context = {'banners':banners, 'most_viewed':most_viewed, 'most_used':most_used, 'searchbar_word':searchbar_word, 'all_most_viewed_banner':all_most_viewed_banner, 'all_most_used_banner':all_most_used_banner}
    return render(request, 'discover-banner.html', context)

#def downloadBanner(request)

