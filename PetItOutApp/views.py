from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from PetItOutApp.forms import UserForm, UserProfileForm,PetProfileForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from PetItOutApp.models import UserProfile,PetProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from PetItOutApp.bing_search import run_query

def home_page(request):
    pet_profile = PetProfile.objects.get(userprofile__user=request.user)
    return render(request, 'PetItOut/home_page.html',{'pet_profile':pet_profile})

def search(request):
    result_list = []
    query = ''

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = run_query(query)

    return render(request, 'PetItOut/search.html', {'result_list': result_list, 'query': query})

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
            # redirect(reverse('PetItOut:home_page'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'PetItOut/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def edit_profile(request,username):
    username = request.user.username
    pet_profile_user = PetProfile.objects.get(userprofile__user=request.user)
    pet_form = PetProfileForm(request.POST or None, request.FILES or None, instance=pet_profile_user)
    if pet_form.is_valid():
        pet_form.save()
        redirect(reverse("PetItOut:user_profile" ,args=[username]))
    return render(request, 'PetItOut/edit_profile.html', context = {'pet_form':pet_form, 'username':username,})
        # current_user = User.objects.get(id = request.user.id)
        # profile_user = UserProfile.objects.get(user_id=request.user.id)
        # username = request.user.username
        
        # user_profile_form = EditProfileForm(request.POST,instance=current_user)
        # pet_profile_form = PetProfileForm(request.POST,instance=profile_user)

        # if user_profile_form.is_valid() and pet_profile_form.is_valid():
        #     user_profile_form.save()
        #     pet_profile_form.save()

        #     login(request,current_user)
        #     return redirect(reverse("PetItOut:user_profile" ,args=[username]))
        
        # else:
        #     print(user_profile_form.errors,pet_profile_form.errors)
    
        # user_profile_form = EditProfileForm()
        # pet_profile_form = PetProfileForm()
        # return render(request, 'PetItOut/edit_profile.html',context = {'user_profile_form':user_profile_form,'pet_profile_form':pet_profile_form,})

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



    
@login_required
def user_profile(request,username):
    try:
        profile = UserProfile.objects.get(user=request.user)
        username = request.user.username
        pet_profile = PetProfile.objects.get(userprofile__user=request.user)
        print(pet_profile.pet_picture)
    except ObjectDoesNotExist:
        messages("This user have no profile!")
        return redirect(reverse('PetItOut:home_page'))
    if request.method == "POST":
    			# Get current user
            current_user_profile = request.user.profile
            current_user_profile.save()
            current_pet_profile = request.user.pet_profile
            current_pet_profile.save()
            response = HttpResponse(mimetype="image/jpg")
            current_pet_profile.save(response,"jpg")
            
    return render(request, "PetItOut/user_profile.html", {"profile":profile,'username':username,'pet_profile':pet_profile})
   

    

@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
    logout(request)
# Take the user back to the homepage.
    return redirect(reverse('PetItOut:home_page'))