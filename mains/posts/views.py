from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/index.html', context)

def new(request):
    return render(request, 'posts/new.html')

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
    context = {
        'post': post
    }
    return render(request, 'posts/edit.html', context)

def update(request, post_id):
    if request.method == "POST":
        edit_title = request.POST.get('edit_title')
        edit_content = request.POST.get('edit_content')
        post = Post.objects.get(pk=post_id)
        post.title = edit_title
        post.content = edit_content
        post.save()
        context = {
            'post': post
        }
        return redirect('posts:show', post_id)
        
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('posts:index')
