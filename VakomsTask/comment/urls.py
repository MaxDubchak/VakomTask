from django.urls import path

from comment.views import post_comment


urlpatterns = [
    path("", post_comment, name='comment'),

]
