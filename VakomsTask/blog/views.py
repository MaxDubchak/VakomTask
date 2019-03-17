"""Blog views module"""
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from blog.models import Blog
from blog.forms import BlogForm


class BlogView(View):
    """Class that handles HTTP requests for blog model."""
    def post(self, request, blog_id=None):
        """Handle the request to create a new blog object."""
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = Blog.create(form.cleaned_data['name'], request.user)
            if not blog:
                return HttpResponse('Database operation failed', status=400)

            return HttpResponseRedirect(reverse('blog', args=[blog.id]))

    def get(self, request, blog_id=None):
        """Handle request to retrieve blog's objects"""
        user = request.user
        if blog_id is not None:
            blog = Blog.get_by_id(id=blog_id)
            posts = blog.get_all_posts_descending()
            return render(request, 'blog_templates/blog.html',
                          {'blog': blog, 'user': user, 'posts': posts})
        else:
            try:
                blog = user.blog.get()
                return HttpResponseRedirect(reverse('blog', args=[blog.id]))
            except (Blog.DoesNotExist):
                form = BlogForm()
                return render(request, 'blog_templates/blog.html',
                              {'form': form})


def get_all_blogs(request):
    """View that handles requests to see all existing blogs"""
    blogs = Blog.get_all_blogs()
    return render(request, 'blog_templates/all_blogs.html', {'blogs': blogs})
