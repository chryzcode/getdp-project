from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mydp_app.views import *

class TestUrls(SimpleTestCase):

    def test_home_urls_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)