from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.published.all()
    return render(
        'blog/post/list.html',
        {'post': posts}
    )
