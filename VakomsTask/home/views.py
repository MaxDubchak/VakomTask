from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def check_auth(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('blog'))
