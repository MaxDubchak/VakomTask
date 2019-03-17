"""This module implements custom middleware."""
from django.http import HttpResponse


class LoginRequiredMiddleware:
    """
    This middleware performs authentication validations in case
    if the path is not available for anonymous users and logged in user.
    """

    def __init__(self, get_response):
        """Initialize middleware instance."""
        self.get_response = get_response

    def __call__(self, request):
        """Provide authentication validations on middleware call."""
        if not request.path_info == '/' and not request.path_info.startswith('/admin'):
            if request.path_info.startswith('/auth'):
                if request.user.is_authenticated:
                    return HttpResponse('Unavailable for authenticated user')

            else:
                if not request.user.is_authenticated:
                    return HttpResponse('Unavailable for unauthenticated user')

        response = self.get_response(request)
        return response
