from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    posts_list = Post.published.all()

    # Norodome kad rodysime tik 3 postus viename puslapyje..

    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        # Jei page_number didesnis nei paginator.num_pages, graziname paskutini puslapi
        
        posts = paginator.page(paginator.num_pages)
        
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})
