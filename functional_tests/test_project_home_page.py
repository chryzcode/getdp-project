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

    def test_home_page_content(self):
        self.browser.get(self.live_server_url)
        intro = self.browser.find_element_by_class_name('intro')
        self.assertEquals(intro.find_element_by_tag_name('h2').text, 'Get Your DP Banner')

    def test_click_banner_redirect_to_view_page(self):
        self.browser.get(self.live_server_url)
        view_banner_url = self.live_server_url + reverse('view-banner', kwargs={'slug': 'testbanner'})
        banner = self.browser.find_element_by_class_name('banner-grid')
        banner.find_element_by_tag_name('a').click()
        self.assertEquals(self.browser.current_url, view_banner_url)


    
