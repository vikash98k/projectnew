from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    roll_no  = models.IntegerField()
    gender  = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
 
    def __str__(self):
        return f'{self.user.username} Profile'

class A(models.Model):
    name = models.CharField(max_length=10)
class B(models.Model):
    secon_name = models.ForeignKey(A,on_delete=models.CASCADE)
    
class C(models.Model):
    first_name = models.ForeignKey(A,on_delete=models.PROTECT)

class Person(models.Model):
    id_value = models.CharField(max_length=10,null=True)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    roll_no  = models.IntegerField()
    gender  = models.CharField(max_length=100)