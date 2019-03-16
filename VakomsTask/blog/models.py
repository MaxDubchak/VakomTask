"""This module implements class that represents blog entity"""
from django.db import models, IntegrityError, OperationalError

from custom_user.models import CustomUser


class Blog(models.Model):
    """Model for Blog entity"""
    name = models.CharField(max_length=64)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog')

    def __str__(self):
        """Method that returns blog instance as string."""
        return f'{self.id} {self.name}'

    def to_dict(self):
        """Method that returns dict with object's attributes."""
        return {
            'id': self.id,
            'name': self.name,
            'user': self.user.id
        }

    @classmethod
    def create(cls, name, user):
        """Method for creating new blog instance"""
        blog = cls()
        blog.name = name
        blog.user = user
        try:
            blog.save()
            return blog
        except(ValueError, IntegrityError, OperationalError) as e:
            print(e)
            return None

    @classmethod
    def get_all_blogs(cls):
        """Method that returns all instances of blog in database"""
        try:
            return cls.objects.all()
        except(IntegrityError, OperationalError):
            return []

    @classmethod
    def get_by_id(cls, id):
        """Method that returns instance of blog found by id"""
        try:
            return cls.objects.get(id=id)
        except(IntegrityError, OperationalError):
            return None

    def get_ordered_posts(self):
        """Method that returns all posts of blog ordered by date"""
        try:
            return self.posts.order_by('posted_date')
        except(ValueError, IntegrityError, OperationalError):
            return []
