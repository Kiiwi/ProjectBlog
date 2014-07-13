from django.shortcuts import render, get_object_or_404
from blogapp.models import Post


def index(request):
    # get the blogapp posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})


def about(request):
    return render(request, 'blog/about.html')