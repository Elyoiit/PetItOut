import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PetItOut.settings")
import django
django.setup()
from PetItOutApp.models import UserProfile, PetProfile, Battle
from django.contrib.auth.models import User


def populate():
    users = [
        {'username' :'henryIsMySon',
        'email' : 'henryIsMySon266@gmail.com',
        'password' : 'thisIsHenrysWorld'}]
    
    user_profiles = [{'username' : 'henryIsMySon',
              'picture': None,
              'userdescription': "Hey everyone!! Im a cat lover with a cat son, and my sons name is henry. There's never been a cat like Henry before and Im here to prove it."}
    ]
    pet_profiles = [{
        'userprofile': 'henryIsMySon',
        'pet_name': 'Henry',
        'pet_type': 'Cat',
        'pet_age': '2 years',
        'pet_description': 'lorem50',
        'pet_picture': None,
    }]

    battles = [{        
        'userprofileRed' : 'henryIsMySon',
        'petprofileRed' : 'Henry',
        'userProfileBlue' : '',
        'petProfileBlue' : ''
    }
    ]

    for user_data in users:
        user = User.objects.create_user(
            username = user_data['username'],
            email = user_data['email'],
            password = user_data['password']
        )
        for user_profile in user_profiles:
            if user_profile['username'] == user.username:
                user_profile_to_add = user_profile
        user_profile_added = add_userprofile(user, user_profile_to_add)

        pet_profiles_to_add = [pet_profile for pet_profile in pet_profiles
                                if pet_profiles['userprofile'] == user_profile_to_add['userprofile']]
        
        for pet_profile in pet_profiles_to_add:
            add_pets(user, user_profile_added, pet_profile)

def add_pets(user, userprofile, pet_profile):
    pet = PetProfile.objects.get_or_create(userprofile = userprofile)[0]
    pet.pet_name = pet_profile['pet_name']
    pet.pet_type = pet_profile['pet_type']
    pet.pet_age = pet_profile['pet_age']
    pet.pet_description = pet_profile['pet_description']
    return pet

def add_userprofile(user, user_profile):
    profile = UserProfile.objects.get_or_create(user = user)[0]
    profile.picture = None
    profile.user_description = user_profile['user_description']
    return profile

if __name__ == '__main__':
    populate()

