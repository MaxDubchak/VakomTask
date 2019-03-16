"""This module implements sending of signup confirmation emails"""
from django.core.mail import send_mail
from utils.JWT_helper import create_token
from django.conf import settings


def send_signup_confirm(email):
    token = create_token(data={'email': email})
    link = f'http://{settings.DOMAIN}/auth/activate/{token}'
    was_sent = send_mail(
        subject='Confirm Sign up',
        message='To confirm your sign up on the VakomsTask web site follow the link ' + link,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    return was_sent
