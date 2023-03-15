from django import forms
from django.contrib.auth.models import User
from PetItOutApp.models import UserProfile

# We could add these forms to views.py, but it makes sense to split them off into their own file.

    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)