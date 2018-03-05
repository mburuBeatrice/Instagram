from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.CharField(max_length =250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.bio
    class Meta:
        ordering = ['bio']
    
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    def update_profile(self):
        self.update()
    def find_profile(name):
        pass   

class Image(models.Model):
    photo = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =250)
    comment = models.CharField(max_length =100)
    profile = models.ForeignKey(Profile)
    likes = models.CharField(max_length =30, null=True, blank=True)


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    def update_caption(self):
        self.update()
    def get_image_by_id(self):
        pass        