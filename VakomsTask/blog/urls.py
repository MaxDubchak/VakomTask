from django.urls import re_path, path

from blog.views import BlogView, get_all_blogs


urlpatterns = [
    path("all", get_all_blogs, name='all_blogs'),
    re_path("(?P<blog_id>\d+)?/?$", BlogView.as_view(), name='blog'),
]
