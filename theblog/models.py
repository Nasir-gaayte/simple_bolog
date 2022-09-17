from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
    
    
    
    def get_absolute_url(self):
        return reverse("home")
     

class Post (models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255, default='The Top')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, max_length=25,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    
    
    def get_absolute_url(self):
        return reverse("home")
     

class Comment(models.Model):
    post=models.ForeignKey(Post, related_name="comments",null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body= models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
    def get_absolute_url(self):
        return reverse("home")
     