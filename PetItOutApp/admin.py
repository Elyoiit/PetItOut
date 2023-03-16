from django.contrib import admin
from PetItOutApp.models import UserProfile,EditProfile,PetProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(EditProfile)
admin.site.register(PetProfile)