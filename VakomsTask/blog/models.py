"""This module implements class that represents blog entity"""
from django.db import models, IntegrityError, OperationalError

from custom_user.models import CustomUser


class Blog(models.Model):
    """Model for Blog entity"""
    blog_name = models.CharField(max_length=64)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog')

    def __str__(self):
        """Method that returns blog instance as string."""
        return f'{self.id} {self.blog_name}'

    def to_dict(self):
        """Method that returns dict with object's attributes."""
        return {
            'id': self.id,
            'blog_name': self.blog_name,
            'user': self.user.id
        }

    @classmethod
    def create(cls, blog_name, user):
        blog = cls()
        blog.blog_name = blog_name
        blog.user = user
        try:
            blog.save()
            return blog
        except(ValueError, IntegrityError, OperationalError):
            return None

