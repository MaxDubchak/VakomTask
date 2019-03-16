from django.urls import re_path, path, include

from blog.views import BlogView, get_all_blogs


urlpatterns = [
    path("all", get_all_blogs, name='all_blogs'),
    path("<int:blog_id>/post/", include('post.urls')),
    re_path("(?P<blog_id>\d+)?/?$", BlogView.as_view(), name='blog'),
]
