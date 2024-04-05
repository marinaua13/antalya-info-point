from django import forms
from django.contrib.auth.forms import UserCreationForm
from catalog.models import Author, Commentary


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        help_text="Required. Inform a valid email address.", required=True
    )

    class Meta:
        model = Author
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "picture"
        ]

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            if picture.size > 10 * 1024 * 1024:
                raise forms.ValidationError("Фотографія занадто велика. Максимальний розмір - 10MB.")
        return picture

    def save(self, commit=True):
        author = super(UserRegistrationForm, self).save(commit=False)
        author.email = self.cleaned_data["email"]
        if 'picture' in self.cleaned_data:
            author.picture = self.cleaned_data['picture']
        if commit:
            author.save()
        print(author.picture)
        return author


class CommentariesForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]


class AuthorsForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = Author
        fields = ["email",
                  "mobile_phone",
                  "years_of_experience",
                  "picture"
                  ]

    def __init__(self, *args, **kwargs):
        super(AuthorsForm, self).__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update({'class': 'form-control'})

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            if picture.size > 10 * 1024 * 1024:
                raise forms.ValidationError("Фотографія занадто велика. Максимальний розмір - 10MB.")
        return picture

