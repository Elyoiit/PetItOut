from django import forms
from django.contrib.auth.models import User
from PetItOutApp.models import UserProfile,  PetProfile

# We could add these forms to views.py, but it makes sense to split them off into their own file.

    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False,)
    class Meta:
        model = UserProfile
        fields = ('picture',)


class PetProfileForm(forms.ModelForm):
    pet_name = forms.CharField(max_length=10,required=False,)
    pet_type = forms.CharField(max_length=500,required=False,)
    pet_age = forms.CharField(required=False,max_length=5,)
    pet_description= forms.CharField(max_length=500,required=False,)
    pet_picture = forms.ImageField(required=False,)
    class Meta:
        model = PetProfile
        fields = ('pet_name','pet_type','pet_age','pet_description','pet_picture')
