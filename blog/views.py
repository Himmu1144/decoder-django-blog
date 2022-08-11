from django.http import HttpResponse
from django.shortcuts import render 
from .models import Post


# Create your views here.

def blogHome(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    if post:
        pass
    else:
        return HttpResponse('404 ERROR | Page Not Found!')
    context = {'post':post}
    return render(request,'blog/blogPost.html', context)