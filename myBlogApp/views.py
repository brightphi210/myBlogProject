from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Blog, Comment

# Create your views here.

def home(request):
    blogPost = Blog.objects.all().order_by('-id')
    comments = Comment.objects.all().order_by('-id')

    return render(request, 'home.html', {'blogs': blogPost, 'comments': comments})


def dashboard(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.POST.get('image')

        blogPost = Blog.objects.create(name=name, description=description, image=image)
        if blogPost.is_valid:
            blogPost.save()
            return redirect('/')
    return render(request, 'dashboard.html')