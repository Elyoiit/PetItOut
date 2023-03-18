from django.contrib import admin
from PetItOutApp.models import UserProfile,PetProfile
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)

# Mix Profile info into User info
class ProfileInline(admin.StackedInline):
	model = UserProfile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	# Just display username fields on admin page
	fields = ["username"]
	inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and Profile
admin.site.register(User, UserAdmin)
admin.site.register(PetProfile)