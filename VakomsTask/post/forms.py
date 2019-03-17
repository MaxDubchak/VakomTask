"""Module that implements form for post creation"""
from django import forms


class PostForm(forms.Form):
    """Form used to create blog posts"""
    headline = forms.CharField(max_length=32)
    text = forms.CharField(max_length=512, widget=forms.Textarea)

