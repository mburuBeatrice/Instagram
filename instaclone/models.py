from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse
# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/', null=True,blank=True)
    bio = models.CharField(max_length =250)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.bio
    class Meta:
        ordering = ['bio']
    def get_absolute_url(self):
        return reverse("instaclone:profile_detail", kwargs={"id": self.id})

    # def profile(self):
    #     id = self.kwargs.get("id")
    #     return Profile.objects.get(id=id)
   
class Post(models.Model):
    photo = models.ImageField(upload_to = 'images/', null=True,blank=True)
    name = models.CharField(max_length =30)
    caption = models.TextField(max_length =250)
    comment = models.TextField(max_length =100,null=True,blank=True)
    profile = models.ForeignKey(User,default=1)
    likes = models.CharField(max_length =30, null=True, blank=True)
    lastupdated = models.DateTimeField(auto_now=True,auto_now_add=False,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-timestamp','-lastupdated']
        
    def get_absolute_url(self):
        return reverse("instaclone:post_detail", kwargs={"id": self.id})
