from django.urls import re_path, path, include

from post.views import PostView


urlpatterns = [
    path("<int:post_id>/comment/", include('comment.urls')),
    re_path("(?P<post_id>\d+)?/?$", PostView.as_view(), name='post'),
]
