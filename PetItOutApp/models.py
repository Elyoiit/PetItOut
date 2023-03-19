import random
import string
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import FieldDoesNotExist


# Create your models here.
# Create A User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    picture = models.ImageField(null=True, blank=True, upload_to="user_profile_images")    
    user_description = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.user.username



# A PetProfile with likes field, where user can like a pet, but only once to the same pet
class PetProfile(models.Model):
    userprofile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    pet_name = models.TextField(blank=True,null=True)
    pet_type = models.TextField(blank=True,null=True)
    pet_age = models.TextField(blank=True,null=True)
    pet_description = models.TextField(blank=True,null=True)
    pet_picture = models.ImageField(upload_to='pet_images',blank=False,null=False)
    objects = models.Manager()
    likes = models.ManyToManyField(User,blank=True)
    @property
    def total_likes(self):
        return self.likes.count() 
    
    def __str__(self):
        return self.pet_name

# map two pet profile to a battle
class Battle(models.Model):
    petprofileRed = models.ForeignKey(PetProfile,related_name="petprofileRed",on_delete=models.CASCADE)
    petprofileBlue = models.ForeignKey(PetProfile,related_name="petprofileBlue",on_delete=models.CASCADE)

    def __str__(self):
        return self.petprofileRed.pet_name+self.petprofileBlue.pet_name
    