"""Custom forms for user registration.

This module defines forms that extend Django's authentication
system for additional functionality.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """User registration form with an extra first name field.

    Inherits from Django's built-in UserCreationForm and requires
    users to provide a first name at signup.

    Fields included:
        - username
        - first_name
        - password1
        - password2
    """

    first_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "password1", "password2"]