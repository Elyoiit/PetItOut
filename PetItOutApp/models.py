from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
<<<<<<< HEAD
from django.db.models.signals import post_save
=======
>>>>>>> 67729c197ffb486196b33282b8c1d24edc953810


# Create your models here.
# Create A User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True, upload_to="user_profile_images")    
    user_description = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.user.username

<<<<<<< HEAD
# Create Profile When New User Signs Up
#@receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
# 	if created:
# 		user_profile = UserProfile(user=instance)
# 		user_profile.save()

# post_save.connect(create_profile, sender=User)

=======

class EditProfile(models.Model):
    user_description = models.TextField()
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user_description
>>>>>>> 67729c197ffb486196b33282b8c1d24edc953810


class PetProfile(models.Model):
<<<<<<< HEAD
    userprofile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    pet_name = models.TextField(blank=True,null=True)
    pet_type = models.TextField(blank=True,null=True)
    pet_age = models.TextField(blank=True,null=True)
    pet_description = models.TextField(blank=True,null=True)
    pet_picture = models.ImageField(upload_to='pet_images',blank=True,null=True)
    objects = models.Manager()
    
    # def save(self,*args,**kwargs):
    #     super(UserProfile, self).save(*args,**kwargs)
=======
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    pet_name = models.TextField(blank=True, null=True)
    pet_type = models.TextField(blank=True, null=True)
    pet_age = models.TextField(blank=True, null=True)
    pet_description = models.TextField(blank=True, null=True)
    pet_picture = models.ImageField(upload_to='pet_images', blank=True, null=True)
    objects = models.Manager()

>>>>>>> 67729c197ffb486196b33282b8c1d24edc953810
    def __str__(self):
        return self.pet_name