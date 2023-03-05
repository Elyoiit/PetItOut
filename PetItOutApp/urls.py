from django.urls import path
from PetItOutApp import views

app_name = 'PetItOut'
urlpatterns = [
   path('', views.home_page, name='home_page'),
   path('register/', views.register, name='register'), # New mapping!
   path('login/', views.user_login, name='login'), 
   path('logout/', views.user_logout, name='logout'),
]