from django.db import models
from django.conf import settings
# Create your models here.

class ImageModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.image.url}"