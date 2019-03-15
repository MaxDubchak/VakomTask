"""Authentication views module"""
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.db import DatabaseError, IntegrityError

from utils.JWT_helper import decode_token
from utils.signup_confirm import send_signup_confirm
from custom_user.forms import LoginForm, SignupForm
from custom_user.models import CustomUser

INITIAL_PHONE_NUMBER = {'phone_number': '+380'}


@require_http_methods(['GET', 'POST'])
def log_in(request):
    """View for processing log in, on GET request returns empty form,
     on POST request tries to log user in"""
    if request.method == 'GET':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            credentials = ['username', 'password']
            credentials = [form.cleaned_data[field] for field in credentials]
            user = authenticate(credentials)
            if user is not None:
                login(request, user)

            else:
                return HttpResponse('No active user with this email password combination',
                                    status=400)

    return render(request, 'auth_templates/login.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def sign_up(request):
    """View to process signing up. On GET request renders signup form,
    on POST request tries to create new user, on success sends confirmation email"""
    if request.method == 'GET':
        form = SignupForm(initial=INITIAL_PHONE_NUMBER)
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            user = CustomUser.create(**form.cleaned_data)
            send_signup_confirm(user.email)

    return render(request, 'auth_templates/signup.html', {'form': form})


@require_http_methods(['GET'])
def signup_confirm(request, token):
    """Function that handles signup confirmation from email link.
    On success activates and logs user in"""
    data = decode_token(token)
    if not data:
        return HttpResponse('Invalid access token', status=498)

    user = CustomUser.get_by_email(email=data.get('email'))
    if not user:
        return HttpResponse('No user with this email', status=400)

    try:
        user.is_active = True
        user.save()
        login(request, user)

    except(DatabaseError, IntegrityError):
        return HttpResponse('Database operation failed', status=400)

    return HttpResponse('User successfully activated', status=200)
