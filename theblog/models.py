from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name_plural = "Categories"
  


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=200, default='Testing')
    likes = models.ManyToManyField(User, related_name='blog_bost')


    def total_likes(self):
        return self.likes.count()



    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
  
    class Meta:
        verbose_name_plural = "Posts"


        
