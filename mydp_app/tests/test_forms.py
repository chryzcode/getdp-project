from django.test import TestCase
from mydp_app.forms import *


class TestForms(TestCase):
    def test_signup_form_valid_data(self):
        form = SignupForm(
            data={
                "full_name": "Test User",
                "username": "testuser",
                "email": "alabaolanrewaju13@gmail.com",
                "password1": "testpassword",
                "password2": "testpassword",
            }
        )
        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_data(self):
        form = SignupForm(
            data={
                "full_name": "Test User",
                "username": "testuser",
                "email": "hey",
                "password1": "testpassword",
                "password2": "testpassword12",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
