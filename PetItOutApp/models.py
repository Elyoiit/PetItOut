from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


# Create your models here.
# Create A User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="user_profile_images")    
    user_description = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.user.username

# Create Profile When New User Signs Up
#@receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	if created:
# 		user_profile = UserProfile(user=instance)
# 		user_profile.save()

# post_save.connect(create_profile, sender=User)



class PetProfile(models.Model):
    userprofile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    pet_name = models.TextField(blank=True,null=True)
    pet_type = models.TextField(blank=True,null=True)
    pet_age = models.TextField(blank=True,null=True)
    pet_description = models.TextField(blank=True,null=True)
    pet_picture = models.ImageField(upload_to='pet_images',blank=True,null=True)
    objects = models.Manager()
    likes = models.ManyToManyField(User,blank=True)
    @property
    def total_likes(self):
        return self.likes.count() 
    
    def __str__(self):
        return self.pet_name
    
class Battle(models.Model):
    petprofileRed = models.OneToOneField(PetProfile,on_delete=models.CASCADE,related_name="petprofileRed")
    petprofileBlue = models.OneToOneField(PetProfile,on_delete=models.CASCADE,related_name="petprofileBlue")

    def __str__(self):
        return self.petprofileRed.userprofile.user.username