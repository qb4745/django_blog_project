from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
