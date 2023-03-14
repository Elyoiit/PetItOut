# PetItOut

main page:
html for sidebar
html to have multiple battle summaries
Create xml that stores total likes, pet pic and pet name.
create percentage bar (ajax or java)
make "See detailed battle button" go to detailed battle page
---------------
update the html to use base.html
update the html to take xml for the percentage bar
update the html so pet names, pics etc can be taken from user profiles
every time you load the page, it shows current battles. Most liked at top and least liked at bottom.

Detailed battle Page:
Finish html
----------------
update the html to use base.html
update the html to take xml for the percentage bar
update the html so pet names, pics etc can be taken from user profiles
-----------------
filter so battle only stays on homepage for a week. after a week, battle is shown on archive.
remove percentage bar and remove vote ability
Make page look good with css
Dynamic link

User profile Page:
Create an html template to have Users details at top of page
Create an html template to display a pet's details
Create html to show these templates
------
user data can be input and saved in XML
user data can be read from the database and displayed in the page
Dynamic link

Pet Hall of Fame:
html template to display a pet (inc profile pic, pets name and likes) 
html for displaying all these templates
-----------------------------------
Code that filters to find highest liked pets
Allow page to get data from database
Add link from pet pic to the owners profile
Code that filters to have only certain pet types

General:
Create form for petsCreate 
form for BattlesCreate 
form for usersupdate 
urls.py to include new pagesupdate 
veiws.py to include new pages
Create python anywhere file that auto loads django when someone tries to run the code
-------------
Populate database with a few profiles (populate.py)
-------------
Add a few battles between created profiles (populate.py)
-------------
Make a few battles 'finished' so they're archived.



12C projects for WAD2

base.html prototype finished -> Harry

Login page(login.html, register.html) Prototype Finished-> Harry 

Models.py(for login parts) Finished -> Harry 

Models.py(for db entities) -> Maks

DB populate -> Maks

Views.py (for login parts) Finished-> Harry

Templates (battle page, home, user profiles) -> Elliot

General css -> Elloit


*For django, all css/javascript/images needs to go to 
static folder reference them in the html files using following format
\<link rel="stylesheet" href="{% static 'css/base.css' %}">
(useless anyone has other solutions)

setting.py urls.py and PetItOutApp.urls.py ammended for logins - Harry
