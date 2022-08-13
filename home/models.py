from django.db import models
from django.contrib.auth.models import User
from blog.models import Post
from django.utils.timezone import now

# Create your models here.

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=500,default='')
    phone = models.CharField(max_length=13,default='')
    message = models.TextField(max_length=10000,default='')
    date = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return f'id - {self.id} | name - {self.name}'

