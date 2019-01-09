from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=180)
    location = models.CharField(max_length=180)
    occupants_count = models.IntegerField()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pi = models.ImageField(upload_to = 'profile_pic/')
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)


class Business(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)

