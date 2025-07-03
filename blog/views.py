from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'blog/home.html')

def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/')
    else:
        form = PostForm()
    return render(request, 'blog/post_write.html', {'form': form})

def blog_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_detail.html', {'post': post})