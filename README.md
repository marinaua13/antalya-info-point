# antalya-info-point  :relaxed:
____

## Overview

I present to you the AntalyaInfoPoint resource. The idea of this resource is to turn it into an information hub for those who came to Antalya (Turkey) and decided to stay in Antalya for a long time... 
On the portal you will find:
+ articles with important information that will help you stay legally and save you from possible fines and problems in the future.
+ information part with the names of services and corresponding offers. Here you will find offers from specialists/masters on topics such as: real estate, beauty services, services for your car and more, everything you need for a comfortable life.
+ information part for your leisure time (about beaches, places for walks, about hammam and more).

Also on the site there is an opportunity to create your own service if you are a master of your craft.
The site is a godsend for those who have chosen this fabulous place to live or for temporary residence.
Since I am focused more on backend development, I used the existing template for the entire frontend - material kit.

## Installation

You should have already installed Python.
+	git clone https://github.com/marinaua13/antalya-info-point.git 
+	cd AntalyaInfoPoint
+	python -m venv venv
+	venv/Scripts/activate
+	pip install -r requirements.txt
+	python manage.py migrate 
+	python manage.py runserver

## Features
### What I use in my project:

+	implement login and logout functionality in the project.
+	separate page for registering a new user
+	separate page for creating your own service
+	the ability to create, update, delete a comment for offer
+	the ability to update user page
+	add and update photo for user
+	service search field
+	easy transitions to the necessary pages using linked titles/masters
+	implement templatetags 
+	also available tests for important function

### Check it out:
[Library project deploy to Render](https://antalya-info-point-9.onrender.com)
### Additional data:
You can use data to have possibility to create comments and after delete it or update, Or create new offer.
>username: admin_new

>password: Regit13

Or you can make new registration 
:relaxed:
