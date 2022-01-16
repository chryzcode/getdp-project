from django.test import TestCase, Client
from django.urls import reverse
from mydp_app.models import *

class TestViews(TestCase):

    def test_home(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login(self):
        client = Client()
        response = client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)

    def test_register(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_create_banner(self):
        client = Client()
        response = client.get(reverse('create-banner'))
        self.assertEquals(response.status_code, 302)

    def test_user_profile(self):
        client = Client()
        response = client.get(reverse('user-profile', args=['testuser']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    def test_delete_account(self):
        client = Client()
        response = client.get(reverse('delete-account'))
        self.assertEquals(response.status_code, 302)

    def test_categories(self):
        client = Client()
        response = client.get(reverse('categories'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories.html')

    def test_banner_category(self):
        client = Client()
        response = client.get(reverse('banner-category', args=['test']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'banner_category.html')
