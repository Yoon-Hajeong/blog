from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    return render(request, 'blog/home.html')

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_detail.html', {'post': post})