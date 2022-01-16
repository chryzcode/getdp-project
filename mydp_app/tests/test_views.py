from django.test import TestCase, Client
from django.urls import reverse
from mydp_app.models import *

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.create_banner_url = reverse('create-banner')
        self.user_profile_url = reverse('user-profile', args=['CODE'])

    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)

    def test_register(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_create_banner(self):
        response = self.client.get(self.create_banner_url)
        self.assertEquals(response.status_code, 302)

    def test_user_profile(self):
        response = self.client.get(self.user_profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    # def test_delete_account(self):
    #     client = Client()
    #     response = client.get(reverse('delete-account'))
    #     self.assertEquals(response.status_code, 302)

    # def test_categories(self):
    #     client = Client()
    #     response = client.get(reverse('categories'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'categories.html')

    # def test_banner_category(self):
    #     client = Client()
    #     response = client.get(reverse('banner-category', args=['category_name']))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'banner_category.html')
