"""This module implements class that represents comment entity"""
from django.db import models, IntegrityError, OperationalError
from django.utils import timezone

from custom_user.models import CustomUser
from post.models import Post


class Comment(models.Model):
    """Model for Comment entity"""
    text = models.CharField(max_length=256)
    commented_date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        """Method that returns comment instance as string."""
        return f'{self.id} {self.commented_date}'

    def to_dict(self):
        return{
            'id': self.id,
            'text': self.text,
            'posted_date': self.commented_date,
            'post': self.post.id,
            'user': self.user.id,
        }

    @classmethod
    def create(cls, text, post, user):
        comment = cls()
        comment.text = text
        comment.post = post
        comment.user = user
        comment.commented_date = timezone.now()
        try:
            comment.save()
            return comment
        except(ValueError, IntegrityError, OperationalError):
            return None
