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


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('blog_list')



def blog_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_detail.html', {'post': post})