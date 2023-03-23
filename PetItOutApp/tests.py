from django.test import TestCase
from PetItOutApp.models import UserProfile,  PetProfile,Battle
from PetItOutApp.forms import UserProfileForm, PetProfileForm
import os
import re
import inspect
import tempfile
import PetItOutApp.models
from PetItOutApp import forms
from django.db import models
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields


def create_user_object():
    """
    Helper function to create a User object.
    """
    user = User.objects.get_or_create(username='testuser',
                                      email='test@test.com')[0]
    user.set_password('testabc123')
    user.save()

    return user

def create_userprofile_object():
    user_object = create_user_object()
    userprofile = UserProfile.objects.get_or_create(user=user_object,
                                            picture=tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                            user_description="this is user description")[0]
    userprofile.save()
    return userprofile

def create_petprofile_object():
    userprofile = create_userprofile_object()
    petprofile = PetProfile.objects.get_or_create(userprofile = userprofile,
                                                  pet_name="test",
                                                  pet_type="test",
                                                  pet_age="1",
                                                  pet_description="test",
                                                  pet_picture = tempfile.NamedTemporaryFile(suffix=".jpg").name,
                                                  )
    petprofile.save()
    return petprofile
    

# Create your tests here.
class ModelTest(TestCase):
    def testEnsureProfileContainsImage(self):
        user_profile = UserProfile()
        expected_attributes = {
            'picture': tempfile.NamedTemporaryFile(suffix=".jpg").name,
            'user': create_user_object(),
            'user_description':'this is user description',
        }
        expected_types = {
            'user':models.fields.related.OneToOneField,
            'picture':models.fields.files.ImageField,
            'user_description':models.fields.TextField
        }
        found_count = 0

        for attr in user_profile._meta.fields:
            attr_name = attr.name
            for expected_attr_name in expected_attributes.keys():
               if expected_attr_name == attr_name:
                   found_count +=1
                   self.assertEqual(type(attr),expected_types[attr_name])
                   setattr(user_profile,attr_name,expected_attributes[attr_name])
        self.assertEqual(found_count,len(expected_attributes.keys()))
        user_profile.save()
    
    def testPetProfileTest(self):
        pet_profile = PetProfile()
        expected_attributes = {
            'userprofile':create_userprofile_object(),
            'pet_name':"jack",
            'pet_type':'dog',
            'pet_age':'18',
            'pet_description':'nothing',
            'pet_picture':tempfile.NamedTemporaryFile(suffix=".jpg").name,
        }
        expected_types = {
            'userprofile':models.fields.related.OneToOneField,
            'pet_name':models.fields.TextField,
            'pet_type':models.fields.TextField,
            'pet_age':models.fields.TextField,
            'pet_description':models.fields.TextField,
            'pet_picture':models.fields.files.ImageField,
            'likes':models.ManyToManyField,
        }
        found_count = 0
        for attr in pet_profile._meta.fields:
            attr_name = attr.name
            for expected_attr_pet_name in expected_attributes.keys():
                if expected_attr_pet_name == attr_name:
                    found_count +=1
                    self.assertEqual(type(attr),expected_types[attr_name])
                    setattr(pet_profile,attr_name,expected_attributes[attr_name])
        self.assertEqual(found_count,len(expected_attributes.keys()))
        pet_profile.save()
    
    
    def testBattleTest(self):
        battle = Battle
        expected_attributes = {
            'petprofileRed':create_petprofile_object,
            'petprofileBlue':create_petprofile_object,
        }
        expected_types = {
            'petprofileRed':models.ForeignKey,
            'petprofileBlue':models.ForeignKey,
        }
        found_count = 0
        for attr in battle._meta.fields:
            attr_name = attr.name
            for expected_attr_pet_name in expected_attributes.keys():
                if expected_attr_pet_name == attr_name:
                    found_count +=1
                    self.assertEqual(type(attr),expected_types[attr_name])
                    setattr(battle,attr_name,expected_attributes[attr_name])
        self.assertEqual(found_count,len(expected_attributes.keys()))
        
class FormTest(TestCase):
    def test_UserProfile(self):
        user_profile_form = UserProfileForm()
        self.assertEqual(type(user_profile_form.__dict__['instance']),UserProfile)

        fields = user_profile_form.fields

        expected_fields = {
            'picture': django_fields.ImageField,
        }
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))


    def test_PetProfile(self):
        pet_profile_form = PetProfileForm()
        self.assertEqual(type(pet_profile_form.__dict__['instance']),PetProfile)

        fields = pet_profile_form.fields

        expected_fields = {
            'pet_name':models.fields.TextField,
            'pet_type':models.fields.TextField,
            'pet_age':models.fields.TextField,
            'pet_description':models.fields.TextField,
            'pet_picture':models.fields.files.ImageField
        }
        for expected_field_name in expected_fields:
            self.assertTrue(expected_field_name in fields.keys())
    
class RegistrationTests(TestCase):

    def test_new_registration_view_exists(self):
        url = ''
        try:
            url = reverse('PetItOut:register')
        except:
            pass

        self.assertEqual(url, '/PetItOut/register/')
    
    def test_bad_registration_post_response(self):
        request = self.client.post(reverse('PetItOut:register'))
        content = request.content.decode('utf-8')

        self.assertTrue('<ul class="errorlist">' in content)

    def test_good_form_creation(self):
        user_data = {'username': 'testuser', 'password': 'test123', 'email': 'test@test.com'}
        user_form = forms.UserForm(data=user_data)
        user_profile_data = {'picture': tempfile.NamedTemporaryFile(suffix=".jpg").name}
        user_profile_form = forms.UserProfileForm(data=user_profile_data)
        self.assertTrue(user_profile_form.is_valid())
        user_object = user_form.save()
        user_object.set_password(user_data['password'])
        user_object.save()
        user_profile_object = user_profile_form.save(commit=False)
        user_profile_object.user = user_object
        user_profile_object.save()
        self.assertTrue(user_form.is_valid())
        self.assertEqual(len(UserProfile.objects.all()),1)
        self.assertTrue(self.client.login(username='testuser', password='test123'))



class LoginTests(TestCase):
    def test_login_url_exists(self):
        url = ''

        try:
            url = reverse('PetItOut:login')
        except:
            pass
        
        self.assertEqual(url, '/PetItOut/login/')

    def test_login_functionality(self):
        user_object = create_user_object()

        response = self.client.post(reverse('PetItOut:login'), {'username': 'testuser', 'password': 'testabc123'})
        
        try:
            self.assertEqual(user_object.id, int(self.client.session['_auth_user_id']))
        except KeyError:
            self.assertTrue(False)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('PetItOut:home_page'))
