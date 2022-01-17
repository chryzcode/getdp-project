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

        self.user = User.objects.create(
            full_name='Test User',
            username='testuser',
            email='testuser@gmail.com',
        )

        self.category = Category.objects.create(
            name='testcategory',
        )

        self.tag = Tag.objects.create(
            name='testtag',
        )

        self.banner = Banner.objects.create(
            name='Test Banner',
            description='Test Description',
            category='testcategory',
            user= self.user,
            slug= 'testbanner',
            tag='testtag',

        )

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
        response = self.client.get(reverse('user-profile', args=['testuser']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-profile.html')

    def test_delete_account(self):
        response = self.client.get(reverse('delete-account'))
        self.assertEquals(response.status_code, 302)

    def test_categories(self):
        response = self.client.get(reverse('categories'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories.html')

    def test_banner_category(self):
        response = self.client.get(reverse('banner-category', args=['testcategory']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'banner-category.html')
