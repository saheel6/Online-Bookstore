from django.db import models

# Create your models here.

class Books(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=400)
    author=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    price=models.IntegerField()
    picture=models.ImageField(upload_to='book_images')