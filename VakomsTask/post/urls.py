from django.urls import re_path, path, include

from post.views import PostView


urlpatterns = [
    re_path("(?P<post_id>\d+)?/?$", PostView.as_view(), name='post'),
]
