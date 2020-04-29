from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/index.html', context)

def new(request):
    form = PostForm()
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, 'posts/new.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title = title, content = content)
        post.save()
        return redirect('posts:index')

def show(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(request, 'posts/show.html', context)

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'posts/edit.html', context)

def update(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
        return redirect('posts:show', post_id)

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:index')
