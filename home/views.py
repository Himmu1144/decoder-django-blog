from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from blog.models import Post
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    
    if request.method=='POST':
        name = request.POST.get('name',default='')
        email = request.POST.get('email',default='')
        phone = request.POST.get('phone',default='')
        message = request.POST.get('message',default='')   

        if len(name)<1 or len(email)<5 or len(phone)<10:
            messages.error(request,'Please fill your form correctly!')
        else:
            contact = Contact(name=name,email=email,phone=phone,message=message)
            contact.save()
            messages.success(request,'Your form has been submitted, We will contact you soon!')

    return render(request, 'home/contact.html')


def search(request):
    query = request.GET.get('query')
    if query == '' or len(query)>120:
        allposts = []
    else:
        allposts = Post.objects.filter(Q(title__icontains=query)|Q(message__icontains=query)|Q(author__icontains=query))
    # if not(allposts):
    #     return HttpResponse('no results found!')
    context = {'allposts':allposts,'query':query}
    return render(request, 'home/search.html',context)

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        # checking the errors in form fillup
        if len(username) > 16:
            messages.error(request,'username can not be greater than 15 characters')
            return redirect('home')

        if not(fname.isalnum() and lname.isalnum()):
            messages.error(request,'Please write the name correctly!')
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,'username should only contain letters and numbers')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request,'Passwords do not match')
            return redirect('home')


        # creating user
        my_user = User.objects.create_user(username,email,pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.save()
        messages.success(request,'Your Account has been Created!')

        return redirect('home')
    else:
        return HttpResponse('404 | Page Not Found!')

def handleLogin(request):

    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')
    
        user = authenticate(username=loginusername,password=loginpassword)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged In!')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials!')
            return redirect('home')
        
    return HttpResponse('404 Not Found!')

def handleLogout(request):
    logout(request)
    messages.success(request,'You are logged out successfully!')
    return redirect('home')
