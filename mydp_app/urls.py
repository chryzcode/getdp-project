from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('create-banner/', views.createBanner, name='create-banner'),
    path('profile/<username>/', views.userProfile, name='user-profile'),
    path('delete-account/', views.deleteAccount, name='delete-account'),
    path('banner/categories/', views.Categories, name='categories'),
    path('use-banner/<slug:slug>/', views.useBanner, name='use-banner'),
    path('banner/category/<str:category_name>/', views.bannerCategory, name='banner-category'),  
    path('banner/<slug:slug>/', views.viewBanner, name='view-banner'),
]