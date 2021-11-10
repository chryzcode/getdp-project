from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('create-banner/', views.createBanner, name='create-banner'),
    path('profile/<username>/', views.userProfile, name='user-profile'),
    path('profile/<username>/edit/', views.editUserProfile, name='edit-user-profile'),
]