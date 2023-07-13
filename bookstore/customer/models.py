from django.db import models
from store.models import Books
from django.contrib.auth.models import User
from django.contrib.auth.models import User

# Create your models here.

class cart(models.Model):
    Books=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='cart')



class Orders(models.Model):
    Books=models.ForeignKey(Books,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=500)
    phone=models.IntegerField()

    options={

          ("order placed","order placed"),
        ("shipped","shipped"),
        ("out for delivery","out for delivery"),
        ("deliverd","delivered"),
        ("cancel","cancel")

    }

    status=models.CharField(max_length=100,choices=options,default="order placed")
    date=models.DateField(auto_now_add=True)

    

