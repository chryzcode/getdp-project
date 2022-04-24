from django.urls import path
from . import views

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
    path("create-category/", views.createCategory, name="create-category"),
    path("delete-category/<str:pk>/", views.deleteCategory, name="delete-category"),
    path("create-tag/", views.createTag, name="create-tag"),
    path("delete-tag/<str:pk>/", views.deleteTag, name="delete-tag"),
    path("all-tags/", views.allTags, name="all-tags"),
    path("all-categories/", views.allCategories, name="all-categories"),
]
