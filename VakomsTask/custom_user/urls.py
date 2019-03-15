from django.urls import path, re_path

from custom_user.views import log_in, sign_up, signup_confirm

urlpatterns = [
    path('', log_in, name='login'),
    path('signup', sign_up, name='signup'),
    re_path(r'^activate/(?P<token>.+)$', signup_confirm, name='signup_confirm'),
]
