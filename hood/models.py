from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Hood(models.Model):
    name = models.CharField(max_length=180)
    location = models.CharField(max_length=180)
    occupants_count = models.IntegerField()
    
    
    def __str__(self):
        return self.name

    def save_hood(self):
        self.save()
    
    def create_hood(self):
        self.create()

    def delete_hood(self):
        self.delete()

    def update_hood(self,id):
        hood = Hood.objects.filter(hood_id = id).update
        return hood
    def update_occupant(self,occupants_count):
        occupant_count = Hood.objects.filter().update()
        return occupant_count




class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = 'profile_pic/')
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    bio = models.TextField()

    def save_profile(self):
        self.save()

    def delet_profile(self):
        self.delete()


class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.email

    def save_business(self):
        self.save()

    def delete_business():
        self.delete()

    def update_business(self,id):
        business = Business.objects.filter(business_id = id).update()
        return business


class Post(models.Model):
    title = models.CharField(max_length = 256)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()



    

