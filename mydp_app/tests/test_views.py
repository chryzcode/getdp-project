from django.test import TestCase, Client
from django.urls import reverse
from mydp_app.models import *

class TestViews(TestCase):

    def test_home(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mydp_app/home.html')