
# CRUD API WITH DJANGO REST FRAMEWORK

Django REST framework is a powerful and flexible toolkit for building Web APIs.

Django is based on MVT (Model View Template) architecture and revolves around CRUD (Create, Retrieve, Update, Delete) operations. CRUD can be best explained as an approach to building a Django web application. In general CRUD means performing Create, Retrieve, Update and Delete operations on a table in a database

![Screenshot from 2021-12-11 11-05-57](https://user-images.githubusercontent.com/83909801/145689988-26091977-c734-4505-9949-140ca5a95737.png)



This is the code repository for project pythonproject using Django rest framework

I have used Django rest framework to create CURD operations

I have also uses alternate method to create CRUD interfaces for a Article model do please check...
Setup Instructions

whatever any IDE your wish like pycharm, vscode and sublime
Requirements

    Python - 3 and above
    sqlite

First make sure that you have the following installed.


### Installation:

    1.pip install django
    2.pip install djangorestframework 

    INSTALLED_APPS = [
        'articleapp',
        'rest_framework',
        'rest_framework.authtoken',
    ]

### Database migration

    $ python manage.py makemigrations
    $ python manage.py migrate

### Run server

    $ python manage.py runserver
    



    
