from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from .forms import PasswordResetForm, PasswordResetConfirmForm
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("create-banner/", views.createBanner, name="create-banner"),
    path("profile/<username>/", views.userProfile, name="user-profile"),
    path("banner/categories/", views.Categories, name="categories"),
    path(
        "banner/category/<str:category_name>/",
        views.bannerCategory,
        name="banner-category",
    ),
    path("banner/<slug:slug>/", views.viewBanner.as_view(), name="view-banner"),
    path("banner/<slug:slug>/edit/", views.editBanner, name="edit-banner"),
    path("banner/<slug:slug>/delete/", views.deleteBanner, name="delete-banner"),
    path("preview/banner/<slug:slug>/", views.previewBanner, name="preview-banner"),
    path("discover-banner/", views.discoverPage, name="discover-page"),
    path("use-banner/<slug:slug>/", views.useBanner, name="use-banner"),
    path("delete-account/<username>", views.deleteAccount, name="delete-account"),
    path(
        "password-reset/password-reset-email-confirm/",
        TemplateView.as_view(template_name="registration/password-reset-success.html"),
        name="password-reset-done",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password-reset-form.html",
            success_url=reverse_lazy("password-reset-done"),
            html_email_template_name="registration/password-reset-email.html",
            form_class=PasswordResetForm,
            
        ),
        name="password-reset",
    ),
    path(
        "password-reset-confirm/MQ/password-reset-complete/",
        TemplateView.as_view(template_name="registration/password-reset-success.html"),
        name="password-reset-complete",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password-reset-confirm.html",
            success_url=reverse_lazy("password-reset-complete"),
            form_class=PasswordResetConfirmForm,
        ),
        name="password-reset-confirm",
    ),
]
