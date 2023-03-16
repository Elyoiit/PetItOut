from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from PetItOutApp.forms import UserForm, UserProfileForm,EditProfileForm,PetProfileForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from PetItOutApp.models import UserProfile,EditProfile,PetProfile

def home_page(request):
    return render(request, 'PetItOut/home_page.html')



def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                profile.save()
                registered = True
        else:
                print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'PetItOut/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
# Use Django's machinery to attempt to see if the username/password
# combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
# If we have a User object, the details are correct.
# If None (Python's way of representing the absence of a value), no user
# with matching credentials was found.
        if user:
# Is the account active? It could have been disabled.
            if user.is_active:
# If the account is valid and active, we can log the user in.
# We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('PetItOut:home_page'))
            else:
# An inactive account was used - no logging in!
                return HttpResponse("Your PetItOut account is disabled.")
        else:
# Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'PetItOut/login.html')
    
def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")
    
@login_required
def user_profile(request):
    username1 = request.user.username
    username=UserProfile.objects.all()
    pet_profile = PetProfile.objects.all()
    return render(request,'PetItOut/user_profile.html',context={'username':username,'pet_profile':pet_profile,'name':username1})
    # user_profile_form = UserProfileForm(request.GET)
    # pet_profile_form = PetProfileForm(request.GET)
    # if user_profile_form.is_valid() and pet_profile_form.is_valid():
    #     return render(request, 'PetItOut/user_profile.html',{
    #                                                                        'pet_name':pet_profile_form.cleaned_data["pet_name"],
    #                                                                        'pet_type':pet_profile_form.cleaned_data["pet_type"],})
    # else:
    #     user_profile_form = UserProfileForm()
    #     pet_profile_form = PetProfileForm()
    
    # return render(request,'PetItOut/user_profile.html',{'user_name':'This Field is Empty',
    #                                                                        'pet_name':'This Field is Empty',
    #                                                                        'pet_type':'This Field is Empty',
    #                                                                        'pet_age':'This Field is Empty',
    #                                                                        'pet_description':'This Field is Empty',
    #                                                                        'pet_picture':'This Field is Empty',
    #                                                                        })                                                          

@login_required
def edit_profile(request):
    if request.method=='POST':
        user_profile_form = EditProfileForm(request.POST)
        pet_profile_form = PetProfileForm(request.POST)

        if user_profile_form.is_valid() and pet_profile_form.is_valid():
            user_profile_form.save()
            pet_profile_form.save()
            if'pet_picture' in request.FILES:
                pet_profile_form.pet_picture=request.FILES['pet_picture']
                pet_profile_form.save()
        else:
            print(user_profile_form.errors,pet_profile_form.errors)
    else:
        user_profile_form = EditProfileForm()
        pet_profile_form = PetProfileForm()
    return render(request, 'PetItOut/edit_profile.html',context = {'user_profile_form':user_profile_form,'pet_profile_form':pet_profile_form,})

    

@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
    logout(request)
# Take the user back to the homepage.
    return redirect(reverse('PetItOut:home_page'))