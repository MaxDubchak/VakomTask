from django.urls import path, include

from home.views import check_auth


urlpatterns = [
    path('', check_auth, name='home'),
]
