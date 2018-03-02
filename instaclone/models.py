from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.CharField(max_length =30)
    name = models.CharField(max_length =30)
    caption = models.CharField(max_length =250)
    comment = models.CharField(max_length =100)


