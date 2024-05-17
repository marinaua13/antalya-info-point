from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from catalog.forms import UserRegistrationForm, AuthorsForm


class UserRegistrationFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "picture": None,
        }
        form = UserRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        invalid_email_form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "invalidemail",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "picture": None,
        }
        invalid_email_form = UserRegistrationForm(data=invalid_email_form_data)
        self.assertFalse(invalid_email_form.is_valid())

        non_matching_passwords_form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password1": "testpassword123",
            "password2": "differentpassword",
            "picture": None,
        }
        non_matching_passwords_form = UserRegistrationForm(
            data=non_matching_passwords_form_data
        )
        self.assertFalse(non_matching_passwords_form.is_valid())


class AuthorsFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "email": "test@example.com",
            "mobile_phone": "+1234567890",
            "years_of_experience": 5,
            "picture": SimpleUploadedFile(
                "file.jpg", b"file_content", content_type="image/jpeg"
            ),
        }
        form = AuthorsForm(data=form_data)
        self.assertTrue(form.is_valid())
