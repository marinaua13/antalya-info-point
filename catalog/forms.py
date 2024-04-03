from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Author, Commentary


class AuthorsForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False
    )  # Додаємо поле для завантаження фотографії

    class Meta:
        model = Author
        fields = ["email", "mobile_phone", "years_of_experience"]

    def __init__(self, *args, **kwargs):
        super(AuthorsForm, self).__init__(*args, **kwargs)
        self.fields["picture"].widget.attrs.update(
            {"class": "form-control"}
        )  # Додаємо клас форми для стилізації

    def clean_picture(self):
        picture = self.cleaned_data.get("picture", None)
        if picture:
            if picture.size > 10 * 1024 * 1024:  # Перевірка розміру фотографії (10MB)
                raise forms.ValidationError(
                    "Фотографія занадто велика. Максимальний розмір - 10MB."
                )
        return picture


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text="Required. Inform a valid email address.", required=True
    )
    picture = forms.ImageField(label="Profile Picture", required=False)

    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "picture",  # Додайте поле picture до списку полів форми
        ]

    def save(self, commit=True):
        author = super(UserRegistrationForm, self).save(commit=False)
        author.email = self.cleaned_data["email"]
        if "picture" in self.cleaned_data:
            author.picture = self.cleaned_data["picture"]
        if commit:
            author.save()
        return author


class CommentariesForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
