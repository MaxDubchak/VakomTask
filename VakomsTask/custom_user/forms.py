"""Module that implements forms for user authentication"""
from django import forms

from custom_user.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'phone_number')
        labels = {
            'first_name': 'first name',
            'last_name': 'last name',
            'phone_number': 'phone number'
        }
        widgets = {
            'password': forms.PasswordInput
        }
