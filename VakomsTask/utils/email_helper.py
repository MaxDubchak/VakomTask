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


def send_on_comment_email(post, comment):
    user = post.blog.user
    link = f'http://{settings.DOMAIN}/blog/{post.blog.id}/post/{post.id}'
    was_sent = send_mail(
        subject='Your post on blog was commented',
        message=f'{user.username}, your post {post.headline} '
        f'was commented by {comment.user.username}, '
        f'checkout this link to see post with the comment {link}',

        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
    return was_sent
