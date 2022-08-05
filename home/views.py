from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact
from django.contrib import messages
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