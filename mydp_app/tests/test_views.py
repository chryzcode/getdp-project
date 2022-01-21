from django.test import TestCase, Client
from django.urls import reverse
from mydp_app.models import User, Banner, Comment, Category, Tag, UserBanner

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
            password='testpassword',
        )

        self.category = Category.objects.create(
            name='testcategory',
            image='testimage.jpg',
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
            image='testimage.jpg',
        )

        self.user_banner = UserBanner.objects.create(
            user=self.user,
            banner=self.banner,
            image='testimage.jpg',
            full_name='Test User',
        )

    def test_create_banner(self):
        response = self.client.post(self.create_banner_url, {
            'name': 'Test Banner',
            'description': 'Test Description',
            'category': 'testcategory',
            'user': self.user,
            'tag': 'testtag',
            'image': 'testimage.jpg',
        })
        self.assertEquals(response.status_code, 302)

    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')  

    
    def test_user_profile(self):
        response = self.client.get(reverse('user-profile', args=[self.user.username]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-profile.html')

    def test_categories(self):
        response = self.client.get(reverse('categories'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories.html')

    def test_banner_category(self):
        response = self.client.get(reverse('banner-category', args=['testcategory']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'banner-category.html')

    def test_view_banner(self):
        response = self.client.get(reverse('view-banner', args=['testbanner']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'view-banner.html')
  
        
    def test_delete_banner(self):
        response = self.client.delete(reverse('delete-banner', args=['testbanner']))
        self.assertEquals(response.status_code, 302)


    def test_preview_banner(self):
        response = self.client.get(reverse('preview-banner', args=['testbanner']))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'preview-banner.html')

    def test_discover_page(self):
        response = self.client.get(reverse('discover-page'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'discover-banner.html')

    def test_create_user_banner(self):
        response = self.client.post(reverse('use-banner', args=['testbanner']), {
            'user': self.user,
            'banner': self.banner,
            'image': 'testimage.jpg',
            'full_name': 'Test User',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user_banner.full_name, 'Test User')
        self.assertEquals(self.user_banner.banner, self.banner)


    def test_register(self):
        response = self.client.post(self.register_url, {
            'full_name': 'Olanrewaju Alaba',
            'username': 'code',
            'email': 'alabaolanrewaju13@gmail.com',
            'password1': 'flyingaway13',
            'password2': 'flyingaway13',
        })
        self.assertEquals(response.status_code, 302)

    def test_logout(self):
        response= self.client.post(self.logout_url, {'email':'alabaolanrewaju13@gmail.com', 'password':'flyingaway13'})
        self.assertEquals(response.status_code, 302)

    def test_logged_out_user_was_redirected(self):
        self.client.login(email='testuser@gmail.com', password='testpassword')
        response = self.client.post(reverse('logout'))
        self.assertEquals(response.status_code, 302)

    def test_logout_redirect_succeeds(self):
        self.client.login(email='testuser@gmail.com', password='testpassword')
        response = self.client.post(reverse('logout'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home.html')

    def test_login_page(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login(self):
        register_user = {
            'full_name':'Test User',
            'username':'testuser',
            'email':'testeruser@gmail.com',
            'password1':'testpassword',
            'password2':'testpassword',
        }

        login_user = {
            'email':'testeruser@gmail.com',
            'password':'testpassword',
        }
        response = self.client.post(self.register_url, register_user, format='text/html')
        user = User.objects.filter(email=register_user['email']).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, login_user, format='text/html')
        self.assertEquals(response.status_code, 302)

    # def test_edit_banner(slf):
