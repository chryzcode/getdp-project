from django.test import TestCase
from mydp_app.models import *


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            full_name="Test User",
            username="testuser",
            email="testuser@gmail.com",
            password="testpassword",
        )

        self.category = Category.objects.create(
            name="testcategory",
            image="testimage.jpg",
        )

        self.tag = Tag.objects.create(
            name="testtag",
        )

        self.banner = Banner.objects.create(
            name="Another Banner",
            description="Test Description",
            category="testcategory",
            user=self.user,
            tag="testtag",
            image="testimage.jpg",
        )

    def test_banner_is_slugified_on_creation(self):
        self.assertEquals(self.banner.slug, "another-banner")
