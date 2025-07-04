from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post
from .forms import PostForm

def home(request):
    return render(request, 'blog/home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        
        # 비밀번호 암호화
        user = User.objects.create(
            username=username,
            password=make_password(raw_password)
        )
        return redirect('login')  # 회원가입 후 로그인 페이지로
    return render(request, 'blog/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        
        user = authenticate(request, username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return redirect('/')  # 로그인 성공 시 메인으로
        else:
            return render(request, 'blog/login.html', {'error': '로그인 실패'})
    return render(request, 'blog/login.html')



@login_required(login_url='/blog/login/')
def post_write(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) #로그인 이용자만 가능하도록
            post.author = request.user #로그인 이용자만 가능하도록
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

def post_search(request, tag):
    posts = Post.objects.filter(
        Q(title__icontains=tag) | Q(category__icontains=tag)
    ).order_by('-id')
    return render(request, 'blog/post_search.html', {
        'tag': tag,
        'posts': posts
    })

def post_search(request):
    tag = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=tag) | Q(category__icontains=tag)
    ).order_by('-id')
    return render(request, 'blog/post_search.html', {
        'tag': tag,
        'posts': posts
    })




def blog_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog_detail.html', {'post': post})