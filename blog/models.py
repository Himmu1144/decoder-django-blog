from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=2000)
    message = models.TextField(max_length=50000)
    slug = models.CharField(max_length=1000)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return f'{self.title} | {self.author}'