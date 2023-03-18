from django.urls import path
from PetItOutApp import views

app_name = 'PetItOut'
urlpatterns = [
   path('', views.home_page, name='home_page'),
   path('battle/', views.battle_page, name = 'battle_page'),
   path('register/', views.register, name='register'), # New mapping!
   path('login/', views.user_login, name='login'), 
   path('logout/', views.user_logout, name='logout'),
   path('profile/<str:username>/', views.user_profile, name='user_profile'),
<<<<<<< HEAD
   path('edit_profile/<str:username>',views.edit_profile, name = 'edit_profile'),
=======
   path('edit_profile/',views.edit_profile, name = 'edit_profile'),
   path('search/', views.search, name='search'),
>>>>>>> 67729c197ffb486196b33282b8c1d24edc953810
]