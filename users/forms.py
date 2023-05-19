from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):  # Inherit from UserCreationForm+
    email = forms.EmailField()  # Default required=True

    class Meta:  # Meta class gives us a nested namespace for configurations
        # and keeps the configurations in one place
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]  # Fields we want in our form and in what order


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  # Default required=True

    class Meta:  # Meta class gives us a nested namespace for configurations
        # and keeps the configurations in one place
        model = User
        fields = ["username", "email"]  # Fields we want in our form and in what order


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]
