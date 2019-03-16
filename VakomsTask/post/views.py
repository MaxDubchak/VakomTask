"""Post views module"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View

from post.models import Post
from post.forms import PostForm
from blog.models import Blog


class PostView(View):
    """Class that handles HTTP requests for blog post model."""

    def post(self, request, blog_id, post_id):
        """Handle the request to create a new post object."""
        blog = Blog.get_by_id(id=blog_id)
        form = PostForm(request.POST)
        if form.is_valid():
            post_data = {
                'headline': form.cleaned_data['headline'],
                'text': form.cleaned_data['text']
            }
            post = Post.create(**post_data, blog=blog)
            if not post:
                return HttpResponse('Database operation failed', status=400)

            return HttpResponseRedirect(redirect_to=f'/blog/{blog_id}')

    def get(self, request, blog_id, post_id=None):
        """Handle request to retrieve post objects"""
        if not post_id:
            form = PostForm()
            return render(request, 'blog_templates/add_post.html',
                          {'form': form})

        else:
            post = Post.get_by_id(id=post_id)
            comments = post.get_all_comments_ascending()
            return render(request, 'blog_templates/post.html',
                          {'post': post, 'comments': comments})
