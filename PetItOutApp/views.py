from django.shortcuts import render

def home_page(request):
    return render(request, 'PetItOut/home_page.html')
