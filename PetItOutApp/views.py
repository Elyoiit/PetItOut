from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from PetItOutApp.forms import UserForm, UserProfileForm,PetProfileForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from PetItOutApp.models import UserProfile,PetProfile,Battle
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from PetItOutApp.bing_search import run_query
import json
from django.core.files import File

def home_page(request):
    battle_view = Battle.objects.all
    return render(request, 'PetItOut/home_page.html',context={'battle_views':battle_view})

def battle(request,username):
    username = username
    print(username)
    context_dict = {}
    battle_view = Battle.objects.get(petprofileRed__userprofile__user__username=username)

    context_dict['battle_view'] = battle_view
    if request.method=="POST":
        if request.POST.get('operation') =="like_submit" and request.is_ajax():
            likes_view = get_object_or_404(PetProfile,userprofile__user__username=username)
            likes_view.likes.add(request.user)
            context_dict['pet_profile']=likes_view
            return HttpResponse(json.dumps(context_dict),likes_view__type='application/json')
    likes_view=PetProfile.objects.all
    return render(request,'PetItOut/battle.html',context=context_dict)

def hallOfFame(request):
    pet_profiles = PetProfile.objects.order_by('-likes')[:10]
    print(pet_profiles)
    return render(request,'PetItOut/hall_of_fame.html',context={'pet_profiles':pet_profiles})

def search(request):
    # result_list = []
    # query = ''

    if request.method == 'POST':
        searched = request.POST['searched']
        pet_profiles = PetProfile.objects.filter(pet_name__contains=searched)
        print(pet_profiles)
    #     query = request.POST['query'].strip()

    #     if query:
    #         result_list = run_query(query)   'result_list': result_list, 'query': query

        return render(request, 'PetItOut/search_result.html', context={'searched':searched,'pet_profiles':pet_profiles})
    else:
        return render(request, 'PetItOut/search_result.html', {})

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
def profile_list(request):
    picturefound=False;
    try:
        pet_profiles = PetProfile.objects.all
        picturefound = True
    except ValueError:
        messages("There's no pet in the database")
        redirect(reverse('PetItOut:home_page'))
    return render(request,'PetItOut/profile_list.html',context={'pet_profiles':pet_profiles,'picturefound':picturefound})

@login_required
def edit_profile(request,username):
    username = request.user.username
    try:
        pet_form = PetProfileForm(request.POST or None, request.FILES or None)
    except IntegrityError:
        pet_form = PetProfileForm(request.POST or None, request.FILES or None)
    if pet_form.is_valid():
        try:
            pet_profile_user = PetProfile.objects.get(userprofile__user=request.user)
            pet_form = PetProfileForm(request.POST or None, request.FILES or None, instance=pet_profile_user)
            pet_form.save()
        except:
            profile = UserProfile.objects.get(user__username=username)
            PetProfile.objects.create(userprofile=profile,pet_name=pet_form.cleaned_data['pet_name'],pet_type=pet_form.cleaned_data['pet_type'],pet_age=pet_form.cleaned_data['pet_age'],pet_description=pet_form.cleaned_data['pet_description'],pet_picture=pet_form.cleaned_data['pet_picture'])
        redirect(reverse("PetItOut:user_profile" ,args=[username]))
    return render(request, 'PetItOut/edit_profile.html', context = {'pet_form':pet_form, 'username':username,})
        

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('PetItOut:home_page'))
            else:
                return HttpResponse("Your PetItOut account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'PetItOut/login.html')



    
@login_required
def user_profile(request,username):
    username = username
    if request.method=='POST':
        try:
            pet_profile_red = PetProfile.objects.get(userprofile__user__username=username)
            pet_profile_blue = PetProfile.objects.get(userprofile__user__username=request.user.username)
            Battle.objects.create(petprofileRed=pet_profile_red,petprofileBlue=pet_profile_blue)
        except:
            messages.error(request,"You don't have a pet, or you already started a battle with it")
    print(username)
    print(request.user.username)
    profile = UserProfile.objects.get(user__username=username)
    profileFound=True;
    try:
        pet_profile = PetProfile.objects.get(userprofile__user__username=username)
        profileFound=True;
        print(pet_profile.pet_picture)
    except:
        pet_profile = None
        profileFound=False;

        
    return render(request, "PetItOut/user_profile.html", {"profile":profile,'username':username,'pet_profile':pet_profile,'profileFound':profileFound})
   

    

@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
    logout(request)
# Take the user back to the homepage.
    return redirect(reverse('PetItOut:home_page'))
