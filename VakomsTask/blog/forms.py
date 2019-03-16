"""Module that implements form for blog creation"""
from django import forms

from blog.models import Blog


class BlogForm(forms.ModelForm):
    """Form used to create new blog"""
    class Meta:
        model = Blog
        fields = 'name',
