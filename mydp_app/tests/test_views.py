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
        self.assertTemplateUsed(response, 'login.html')

    def test_logout(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)

    def test_register(self):
        client = Client()
        response = client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_create_banner(self):
        client = Client()
        response = client.get(reverse('create-banner'))
        self.assertEquals(response.status_code, 302)
        