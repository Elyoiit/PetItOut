from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models





# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.user.username
    
class EditProfile(models.Model):
    user_description = models.TextField()
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    def __str__(self):
        return self.user_description

class PetProfile(models.Model):
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    pet_name = models.TextField(blank=True,null=True)
    pet_type = models.TextField(blank=True,null=True)
    pet_age = models.TextField(blank=True,null=True)
    pet_description = models.TextField(blank=True,null=True)
    pet_picture = models.ImageField(upload_to='pet_images',blank=True,null=True)
    objects = models.Manager()
    def __str__(self):
        return self.pet_name



