from django.test import TestCase
from PetItOutApp.models import UserProfile,  PetProfile
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

# Create your tests here.
class ModelTest(TestCase):
    def ensureProfileContainsImage(self):
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

class RegisterFormClassTests(TestCase):
    