"""Module that implements forms for user authentication"""
from django import forms

from custom_user.models import CustomUser


class LoginForm(forms.Form):
    """Form used for user login"""
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):
    """Form used for user registration"""
    class Meta:
        model = CustomUser
        exclude = ['is_superuser', 'is_active', 'is_staff',
                   'groups', 'date_joined', 'user_permissions', 'last_login']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'phone_number': 'Phone number'
        }
        widgets = {
            'password': forms.PasswordInput
        }
