"""This module implements class that represents the user entity."""
from django.contrib.auth.models import AbstractUser
from django.db import models, IntegrityError, OperationalError


class CustomUser(AbstractUser):
    """Model for User entity."""
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    phone_number = models.CharField(max_length=16, blank=True)

    def __str__(self):
        """Method that returns user instance as string."""
        return f'{self.id} {self.username}'

    def to_dict(self):
        """Method that returns dict with object's attributes."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone_number': self.phone_number
        }

    @classmethod
    def create(cls, password, **kwargs):
        """Method used to create """
        user = cls()
        user.set_password(password)
        user.is_active = False
        for key, value in kwargs.items():
            setattr(user, key, value)
        try:
            user.save()
            return user
        except(ValueError, IntegrityError, OperationalError):
            return None

    @classmethod
    def get_by_email(cls, email):
        """Method that returns user by email"""
        try:
            return cls.objects.get(email=email)
        except (ValueError, cls.DoesNotExist, OperationalError):
            return None
