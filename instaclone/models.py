from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to = 'image/')
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =250)
    comment = models.CharField(max_length =100)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    bio = models.CharField(max_length =250)

