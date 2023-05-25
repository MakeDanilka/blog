from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import *
from .forms import PostForm, UserRegisterForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic.list import ListView
from django.db.models import Q


def index(request):
    users = Users.objects.all()
    return render(request, 'girls/index.html', {'users': users})

def girls(request):
    return HttpResponse("страница приложения girls")


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 

    return render(request, 'girls/post_list.html',{'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    #return render(request, 'girls/post_detail.html', {'post': post})

    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'girls/post_detail.html',
                 {'post': post,
                  'comments': comments,
                  'comment_form': comment_form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'girls/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'girls/post_edit.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Создан аккаунт {username}')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request,'girls/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'girls/profile.html',)

def search(request):
    query = request.GET.get('q')
    articles = Post.objects.filter(Q(title=query))
    return render(request, 'girls/serach.html', {'articles': articles, 'query': query})


