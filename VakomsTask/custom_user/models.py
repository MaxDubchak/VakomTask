"""This module implements class that represents the user entity."""
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models, IntegrityError, OperationalError


class CustomUser(AbstractBaseUser):
    """Model for User entity."""
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format:"
                                         " '+380 555555555'. Up to 16 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=16)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = BaseUserManager()

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
