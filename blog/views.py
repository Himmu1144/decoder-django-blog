from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras


# Create your views here.

def blogHome(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comment = BlogComment.objects.filter(post=post,parent=None)
    replyes = BlogComment.objects.filter(post=post).exclude(parent=None)
    repdict = {}
    for reply in replyes:
        if reply.parent.id not in repdict.keys():
            repdict[reply.parent.id] = [reply]
        else:
            repdict[reply.parent.id].append(reply)
    if post:
        pass
    else:
        return HttpResponse('404 ERROR | Page Not Found!')
    context = {'post':post,'comments':comment,'user':request.user,'replyes':repdict}

    return render(request,'blog/blogPost.html', context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        postSno = request.POST.get('postSno')
        replySno = request.POST.get('replySno')
        user = request.user
        post = Post.objects.filter(id=postSno).first()

        if replySno == '':            
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,'Your comment has been succesfully posted!')
        else:
            parent = BlogComment.objects.filter(id=replySno).first()
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,'Your reply has been succesfully posted!')

    return redirect(f'/blog/{post.slug}')

