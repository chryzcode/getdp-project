from selenium import webdriver
from mydp_app.models import *
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectHomePage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        banner_grid = self.browser.find_element_by_class_name('banner-grid')
        intro = self.browser.find_element_by_class_name('intro')
        self.assertEquals(intro.find_element_by_tag_name('h2').text, 'Get Your DP Banner ---')
        time.sleep(2000)