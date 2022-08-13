from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=2000)
    message = models.TextField(max_length=50000)
    slug = models.CharField(max_length=1000)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return f'{self.title} | {self.author}'

class BlogComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField(max_length=10000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.comment[0:50]}...  by {self.user.username}'
   