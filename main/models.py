from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    description = models.TextField(max_length=255, blank=True,null=True)
    
def __str__(self):
    return self.user.username

class Entry(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword

class Comment(models.Model):
    entry = models.ForeignKey(Entry,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reply = models.ForeignKey('self',null=True,related_name='replies',on_delete=models.CASCADE)
    content = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.content


class Star(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    timestamp = models.DateTimeField(auto_now_add=True)
    




    
   





