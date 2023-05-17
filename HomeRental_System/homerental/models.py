import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, unique=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile/', default='profile/user-default.png')
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=500,null=True,blank=True)
    phone = models.CharField(max_length=11,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    is_homeowner = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

class HomeOwner(models.Model):
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
   # renters = models.ForeignKey(Renter, on_delete=None, null=True, blank=True)

    def __str__(self):
       return str(self.user_profile.name)


class Renter(models.Model):
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
   #homeOwner = models.OneToOneField('HomeOwner', on_delete=None, null=True, blank=True)
    homeOwner = models.ForeignKey(HomeOwner, on_delete=models.SET_NULL, null=True, blank=True)




class HomeAdd(models.Model):
    home_type = (
        ('apartment', 'apartment'),
        ('room', 'room')
    )
    home_owner = models.ForeignKey(HomeOwner, on_delete=models.CASCADE)
    renter = models.OneToOneField(Renter, on_delete=models.SET_NULL, null=True, blank=True)
    block_name = models.CharField(max_length=1)
    road_num = models.CharField(max_length=3)
    house_num = models.CharField(max_length=5)
    house_details = models.CharField(max_length=1000)
    house_type = models.CharField(max_length=20, choices=home_type)



class HomeImages(models.Model):
    home = models.ForeignKey(HomeAdd,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(null=True, blank=True, default="default.jpg")


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    reciver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name='messages')
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.body[:30])

    class Meta:
        ordering = ['is_read', '-created']


class Complain(models.Model):
    complainer = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,related_name='complainer')
    complainee = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,related_name='complainee')
    complain = models.TextField()
