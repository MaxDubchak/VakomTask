"""Module that implements form for comment creation"""
from django import forms


class CommentForm(forms.Form):
    """Form used to create blog comments"""
    text = forms.CharField(max_length=256, widget=forms.Textarea)

