from unicodedata import name
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


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = RichTextUploadingField(blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    website = models.CharField(max_length=200,blank=True, null=True)
    facebook = models.CharField(max_length=200,blank=True, null=True)
    twitter = models.CharField(max_length=200,blank=True, null=True)

    #adds to admin area
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    snippet = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=200, default='Testing')
    likes = models.ManyToManyField(User, related_name='blog_bost')


    def total_likes(self):
        return self.likes.count()


#adds to admin area
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')
  
    class Meta:
        verbose_name_plural = "Posts"



class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %  (self.post.title, self.name)



        

