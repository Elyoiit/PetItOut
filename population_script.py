from io import BytesIO
import os

import requests

from PetItOut.settings import MEDIA_DIR, STATIC_DIR
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PetItOut.settings")
import django
django.setup()
from PIL import Image
from PetItOutApp.models import UserProfile, PetProfile, Battle
from django.contrib.auth.models import User
import tempfile

def populate():
    POPULATION_PICTURES_DIR = os.path.join(MEDIA_DIR, "population_images")
    users = [
        {'username' :'HenryIsMySon',
        'email' : 'henryIsMySon266@gmail.com',
        'password' : 'thisIsHenrysWorld'},

        {'username' :'Hannah_Lane',
        'email' : 'HannahLane1997@live.co.uk',
        'password' : '1231997'},
    
        {'username' :'CoffeeBeanGhost',
        'email' : 'BethSimpson@gmail.com',
        'password' : 'GoingGhost'},

        {'username' :'RatPack1562',
        'email' : 'ratfactsbuisiness@yahoo.com',
        'password' : 'MyD0g1sS1ck'},

        {'username' :'LizardLizzie234',
        'email' : 'LizardLizzie@yahoo.com',
        'password' : 'LIzzle'},
        
        {'username' :'A_Streetpet_named_Desire',
        'email' : 'J_Smith1989@Bing.co.uk',
        'password' : 'BestMovieBestPet'},
        
        {'username' :'WholeWorldOnMyBack667',
        'email' : 'WorldBackOnMy@gmail.com',
        'password' : 'BackWorldCarryingThatIDo'},]
        
    user_profiles = [{
            'username' : 'HenryIsMySon',
            'picture': os.path.join(POPULATION_PICTURES_DIR, "henry_is_my_son.jpg"),
            'user_description': "Hey everyone!! Im a cat lover with a cat son, and my sons name is henry. There's never been a cat like Henry before and Im here to prove it."},

            {'username' : 'Hannah_Lane',
            'picture': os.path.join(POPULATION_PICTURES_DIR, "HannahLane.jpg"),
            'user_description': "My name's Hannah lane. I have a love of all things animal and want to see whats going on! I always love to talk to so send me a message if you feel like chatting :)" },

            {'username' : 'CoffeeBeanGhost',
            'picture': os.path.join(POPULATION_PICTURES_DIR, "CoffeeBeanGhost.jpg"),
            'user_description': "I'm mostly here to show off my reptiles. A lot of people are not fans of lizards, but I want to show people that they are cute and way way way sweeter than people think. If you are a fan and want to see more pics of them, then you can find me at 'CoffeeBeanGhost' on instagram"}, 
            
            {'username' : 'RatPack1562',
            'picture': os.path.join(POPULATION_PICTURES_DIR, "fractal_profile_pic.jpg"),
            'user_description': "hi. you might know me from twitter as @ratFacts (and if you dont you should totally follow me) (and if you do know me but arent following me you should also follow me) (if you are following me then yay!). that was too many brackets. like my pets!"},

            {'username' : 'LizardLizzie234',
            'picture': os.path.join(POPULATION_PICTURES_DIR, "LizardLizzie.jpg"),
            'user_description': "i love lizards!!! lizards Are some of the best creature to ever existed. you ever seen a movie about bringing back ancient giant dogs?? didnt think so"},

            {'username' : 'A_Streetpet_named_Desire',
            'picture': os.path.join(POPULATION_PICTURES_DIR, "Tortoise.jpg"),
            'user_description': "Hi everyone! I don't really have much to say about myself, so Ill let my tortoise, Brandon, do the talking (figuratively)"},

            {'username' : 'WholeWorldOnMyBack667',
            'picture': os.path.join(POPULATION_PICTURES_DIR, "Atlas.jpg"),
            'user_description': "Hello. If you've seen Hannah Lane on this app then tell her days as reigning chapion of owner of the cutest pet is over. I know her in real life and she's done nothing but brag, so I'm here to set the record straight"}
    ]

    pet_profiles = [
        {'userprofile': 'HenryIsMySon',
        'pet_name': 'Henry',
        'pet_type': 'Cat',
        'pet_age': '2 years',
        'pet_description': 'Henry is the sweetest, bestest cat you will ever see in your life and Im here to prove it. Seriously, If you dont vote for this little fella then I dont know whats wrong with you. But its something. Something you should go to a doctors about.',
        'pet_picture': os.path.join(POPULATION_PICTURES_DIR, "this_is_henry.jpg")},

        {'userprofile': 'Hannah_Lane',
        'pet_name': 'Ally',
        'pet_type': 'Cat',
        'pet_age': '1 years',
        'pet_description': "Ally is a little standoffish at times, but she means well. She spends most of her time trying to climb on top of doorframes and I spend most of my time trying to get her down",
        'pet_picture': os.path.join(POPULATION_PICTURES_DIR, "ally.jpg")},

        {'userprofile': 'WholeWorldOnMyBack667',
        'pet_name': 'Cierra',
        'pet_type': 'Dog',
        'pet_age': '7 years',
        'pet_description': "Cierra's best friend is Ally. She's a lot calmer and a LOT more cuddly.",
        'pet_picture': os.path.join(POPULATION_PICTURES_DIR, "Cierra.jpg")},

        {'userprofile': 'CoffeeBeanGhost',
        'pet_name': 'Tony',
        'pet_type': 'Snake',
        'pet_age': '1.2 years',
        'pet_description': "If you're a little skittish around snakes then I don't blame you. Media's made them out to be these cold-blooded, heartless creatures. They are cold-blooded and love lounging, but If anyone's told you they're heartless and don't have emotions, that person hasn't owned them",
        'pet_picture': os.path.join(POPULATION_PICTURES_DIR, "snake.jpg")},

        {'userprofile': 'A_Streetpet_named_Desire',
        'pet_name': 'Brandon',
        'pet_type': 'Tortoise',
        'pet_age': '12 years',
        'pet_description': "Please say a little 'hi' to definitely the oldest pet I have. Brandon is a sweet old man who just wants to eat lettice and relax. We could all be a bit more chill in life and Brandon reminds us of that",
        'pet_picture': os.path.join(POPULATION_PICTURES_DIR, "Tortoise.jpg")},

        {'userprofile': 'LizardLizzie234',
        'pet_name': 'Shelley',
        'pet_type': 'Iguana',
        'pet_age': '3 years',
        'pet_description': "Shelley is my iguana. She's definitely a bit spoiled, but she's pretty enough to deserve it. I remember going to the reptile house whenever my parent's would take me to the zoo. I always wanted an iguana the most, so Shelley was the first reptile I ever got. We've been through thick and thin together and she's always going to have a special place in my heart",
        'pet_picture': os.path.join(POPULATION_PICTURES_DIR, "Iguana.jpg")},

        {'userprofile': 'RatPack1562',
        'pet_name': 'Mayo',
        'pet_type': 'Rat',
        'pet_age': '1.2 years',
        'pet_description': "look at this little gentleman. this little guy. how can you not love him. rats are smart but mayo is really really smart. he leanrs to do tricks so quickly its not even funny and he loves to do puzzles to get his food.",
        'pet_picture': os.path.join(POPULATION_PICTURES_DIR, "mouse.jpg")},

    ]

    battles = [
        {'pet_name_red' : 'Shelley',
        'pet_name_blue' : 'Ally'},

        {'pet_name_red' : 'Ally',
        'pet_name_blue' : 'Mayo'},

        {'pet_name_red' : 'Henry',
        'pet_name_blue' : 'Tony'},

        {'pet_name_red' : 'Mayo',
        'pet_name_blue' : 'Shelley'},

        {'pet_name_red' : 'Brandon',
        'pet_name_blue' : 'Cierra'},

        {'pet_name_red' : 'Tony',
        'pet_name_blue' : 'Shelley'},

        {'pet_name_red' : 'Cierra',
        'pet_name_blue' : 'Henry'},

        {'pet_name_red' : 'Tony',
        'pet_name_blue' : 'Brandon'},
    ]

    for user_data in users:
        user = User.objects.create_user(
            username = user_data['username'],
            email = user_data['email'],
            password = user_data['password']
        )
        for user_profile in user_profiles:
            if user_profile['username'] == user.username:
                user_profile_added = add_userprofile(user, user_profile)
                user_profile['object'] = user_profile_added
                username_of_added_account = user_profile['username']

        for pet_profile in pet_profiles:
            if pet_profile['userprofile'] == username_of_added_account:
                pet_profile['object'] = add_pets(user, user_profile_added, pet_profile)

    for battle in battles:
        red_pet = None
        blue_pet = None

        for pet_profile in pet_profiles:
            if pet_profile['pet_name'] == battle['pet_name_red']:
                red_pet = pet_profile['object']
            elif pet_profile['pet_name'] == battle['pet_name_blue']:
                blue_pet = pet_profile['object']
        
        Battle.objects.create(petprofileRed = red_pet,
                            petprofileBlue = blue_pet,
                            battleName = red_pet.pet_name + blue_pet.pet_name)


def add_pets(user, userprofile, pet_profile):
    petprofile = PetProfile.objects.get_or_create(userprofile=userprofile,
                                                   pet_name=pet_profile['pet_name'],
                                                   pet_type=pet_profile['pet_type'],
                                                   pet_age=pet_profile['pet_age'],
                                                   pet_description=pet_profile['pet_description'],
                                                   pet_picture = pet_profile['pet_picture'])[0]
    return petprofile

def add_userprofile(user, user_profile):
    profile = UserProfile.objects.get_or_create(user = user)[0]
    profile.picture = user_profile['picture']
    profile.user_description = user_profile['user_description']
    profile.save()
    return profile

if __name__ == '__main__':
    populate()

