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
        """Method that returns post data as dictionary"""
        return{
            'id': self.id,
            'headline': self.headline,
            'text': self.text,
            'posted_date': self.posted_date,
            'blog': self.blog.id
        }

    @classmethod
    def create(cls, headline, text, blog):
        """Method used to create new post instance"""
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

    @classmethod
    def get_by_id(cls, id):
        """Method that returns instance of post found by id"""
        try:
            return cls.objects.get(id=id)
        except(IntegrityError, OperationalError):
            return None

    def get_all_comments_ascending(self):
        """Method that returns all comments of post ordered by date(ascending)"""
        try:
            return self.comments.order_by('commented_date')
        except(ValueError, IntegrityError, OperationalError):
            return []
