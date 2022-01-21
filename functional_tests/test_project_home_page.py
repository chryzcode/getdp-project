from selenium import webdriver
from mydp_app.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse

class TestProjectHomePage(StaticLiveServerTestCase):
    def test_foo(self):
        self.assertEquals(0, 1)