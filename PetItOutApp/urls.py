from django.urls import path
from PetItOutApp import views

app_name = 'PetItOut'
urlpatterns = [
   path('', views.home_page, name='home_page'),
   path('register/', views.register, name='register'), # New mapping!
   path('login/', views.user_login, name='login'), 
   path('logout/', views.user_logout, name='logout'),
   path('profile/<str:username>/', views.user_profile, name='user_profile'),
   path('profile/edit_profile/<str:username>',views.edit_profile, name = 'edit_profile'),
   path('profile_list/', views.profile_list, name = 'profile_list'),
   path('search/', views.search, name='search'),
   path('battle/<str:username>/',views.battle,name='battle'),
   path('search_result/',views.search,name = 'search'),
   path('hall_of_fame/',views.hallOfFame,name = 'hall_of_fame')
]