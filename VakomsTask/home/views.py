from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def check_auth(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to='/auth/login')
    else:
        return HttpResponseRedirect(redirect_to='/blog')
