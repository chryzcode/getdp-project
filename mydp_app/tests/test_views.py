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

    def test_home(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login(self):
        response = self.client.get(self.login_url, {'email':'testuser@gmail.com', 'password':'testpassword'})
        self.assertEquals(response.status_code, 302)

    def test_logout(self):
        response= self.client.post(self.logout_url, {'email':'testuser@gmail.com', 'password':'testpassword'})
        self.assertEquals(response.status_code, 302) 

    def test_create_banner(self):
        response = self.client.post(self.create_banner_url, {
            'name': 'Another banner',
            'description': 'Another description',
            'category': 'testcategory',
            'user': self.user,
            'image': 'testimage.jpg',

        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.banner.name, 'Another Banner')
        self.assertEquals(self.banner.slug, 'another-banner')

    def test_user_profile(self):
        response = self.client.get(reverse('user-profile', args=[self.user.username]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-profile.html')


    def test_create_user_banner_no_data(self):
        response = self.client.post(self.create_banner_url, {
            'name': '',
            'description': '',
            'category': '',
            'user': '',
            'tag': '',
            'image': '',

        })
        self.assertEquals(response.status_code, 302)

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




    # def test_edit_banner(self):
    #     response = self.client.get(reverse('view-banner', args=['testbanner']))
    #     response = self.client.post(reverse('edit-banner', args=['testbanner']), {
    #         'name': 'Edited Banner',
    #         'description': 'Edited Description',
    #         'category': 'testcategory',
    #         'user': self.user,
    #         'tag': 'testtag',
    #         'image': 'testimage.jpg',
    #         'slug': 'editedbanner',
    #     })
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(self.banner.name, 'Edited Banner')
