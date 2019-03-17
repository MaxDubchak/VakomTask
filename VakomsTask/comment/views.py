"""Post views module"""
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_http_methods

from comment.models import Comment
from post.models import Post
from comment.forms import CommentForm
from utils.email_helper import send_on_comment_email


@require_http_methods(['POST'])
def post_comment(request, blog_id, post_id):
    """Handle the request to create a new comment object."""
    post = Post.get_by_id(post_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        comment = Comment.create(text=text, post=post, user=request.user)
        if not comment:
            return HttpResponse('Database operation failed', status=400)
        was_sent = send_on_comment_email(post, comment)
        if not was_sent:
            return HttpResponse('Unable to send email', status=502)
        return HttpResponseRedirect(redirect_to=f'/blog/{blog_id}/post/{post_id}')
