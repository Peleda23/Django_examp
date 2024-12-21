from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_list(request):
    posts_list = Post.published.all()

    # Norodome kad rodysime tik 3 postus viename puslapyje..

    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)

    # Jei page_number nera skaicius, graziname pirmaji puslapi
    except PageNotAnInteger:
        posts = paginator.page(1)

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


def post_share(request, post_id):
    # Ištraukiam posta pagal id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    if request.method == "POST":
        # Forma buvo panaudota
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Forma praėjo
            cd = form.cleaned_data
            # Siunčiam emaila
        else:
            form = EmailPostForm()
        return render(request, "blog/post/share.html", {"post": post, "form": form})
