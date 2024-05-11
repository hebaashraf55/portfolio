from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from .models import Person, Post
#
# Create your views here.


def home(request):  
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')


def posts(request):
    post = Post.objects.all()
    context= {'post': post}
    return render(request,'myapp/posts.html',context)





