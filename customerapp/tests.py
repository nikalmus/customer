from django.test import TestCase
from django import forms
from customerapp.mixins import ZipCodeValidationMixin

class MockForm(forms.Form):
    zip_code = forms.CharField()

class ZipCodeValidationMixinTestCase(TestCase):
    def setUp(self):
        self.mixin = ZipCodeValidationMixin()

    def test_valid_zip_code(self):
        form = MockForm(data={'zip_code': '12345'})
        form.is_valid()  # Simulate form validation
        is_valid = self.mixin.validate_zip_code(form)
        self.assertTrue(is_valid)
        self.assertEqual(form.errors, {})

    def test_invalid_zip_code(self):
        form = MockForm(data={'zip_code': '1234'})
        form.is_valid()  # Simulate form validation
        is_valid = self.mixin.validate_zip_code(form)
        self.assertFalse(is_valid)
        self.assertEqual(form.errors['zip_code'], ['Enter a valid ZIP code in the format XXXXX or XXXXX-XXXX.'])


    def test_valid_zip_code_with_dash(self):
        form = MockForm(data={'zip_code': '12345-6789'})
        form.is_valid()  # Simulate form validation
        is_valid = self.mixin.validate_zip_code(form)
        self.assertTrue(is_valid)
        self.assertEqual(form.errors, {})

from .models import Customer

class CustomerModelTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(
            first_name="John",
            last_name="Doe",
            address="123 Main St",
            city="Denver",
            zip_code="12345",
            state="CO"
        )


    def test_customer_str_representation(self):
        customer = Customer.objects.get(first_name="John")
        self.assertEqual(str(customer), "John Doe from Denver, CO")

