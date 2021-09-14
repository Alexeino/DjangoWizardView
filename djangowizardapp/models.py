from django.db import models

# Create your models here.

class FormData(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.fname}"