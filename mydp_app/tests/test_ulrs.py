from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mydp_app.views import *

class TestUrls(SimpleTestCase):

    def test_home_urls_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_login_urls_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_logout_urls_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutPage)

    def test_register_urls_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

    def test_create_banner_urls_is_resolved(self):
        url = reverse('create-banner')
        self.assertEquals(resolve(url).func, createBanner)

    def test_user_profile_urls_is_resolved(self):
        url = reverse('user-profile', args=['username'])
        self.assertEquals(resolve(url).func, userProfile)

    def test_delete_account_urls_is_resolved(self):
        url = reverse('delete-account')
        self.assertEquals(resolve(url).func, deleteAccount)

    def test_banner_categories_urls_is_resolved(self):
        url = reverse('categories')
        self.assertEquals(resolve(url).func, Categories)

    def test_banner_category_urls_is_resolved(self):
        url = reverse('banner-category', args=['category_name'])
        self.assertEquals(resolve(url).func, bannerCategory)

    def test_view_banner_urls_is_resolved(self):
        url = reverse('view-banner', args=['slug'])
        self.assertEquals(resolve(url).func.view_class, viewBanner)

    def test_edit_banner_urls_is_resolved(self):
        url = reverse('edit-banner', args=['slug'])
        self.assertEquals(resolve(url).func, editBanner)
    
    def test_delete_banner_urls_is_resolved(self):
        url = reverse('delete-banner', args=['slug'])
        self.assertEquals(resolve(url).func, deleteBanner)

    def test_preview_banner_urls_is_resolved(self):
        url = reverse('preview-banner', args=['slug'])
        self.assertEquals(resolve(url).func, previewBanner)

    def test_discover_banner_urls_is_resolved(self):
        url = reverse('discover-page')
        self.assertEquals(resolve(url).func, discoverPage)