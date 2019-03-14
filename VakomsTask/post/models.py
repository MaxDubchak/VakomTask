"""This module implements class that represents blog's post entity"""
from django.db import models, IntegrityError, OperationalError
from django.utils import timezone

from blog.models import Blog


class Post(models.Model):
    """Model for Post entity"""
    posted_date = models.DateTimeField()
    headline = models.CharField(max_length=32)
    text = models.CharField(max_length=512)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        """Method that returns post instance as string."""
        return f'{self.id} {self.posted_date}'

    def to_dict(self):
        return{
            'id': self.id,
            'headline': self.headline,
            'text': self.text,
            'posted_date': self.posted_date,
            'blog': self.blog.id
        }

    @classmethod
    def create(cls, headline, text, blog):
        post = cls()
        post.headline = headline
        post.text = text
        post.blog = blog
        post.posted_date = timezone.now()
        try:
            post.save()
            return post
        except(ValueError, IntegrityError, OperationalError):
            return None
