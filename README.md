# Django 5 Starter Template

## Requirements

* Django 5
* Python 3.10+

## Instructions

Create the project folder:

    mkdir <project_name>
    
Enter the directory and initiate a virtual env:

    cd <project_name>
    python -m venv .venv

Load the virtualenv:

    source .venv/bin/activate

Install Django:

    pip install django

Create a django project:

    django-admin startproject --template=https://bit.ly/47BCyij --extension=py,sh,env <project_name> .

Execute the startup script:

    ./start.sh
    
Install all the dependencies:

    pip install -r requirements/dev.txt
    
Run all the migrations:

    python manage.py migrate
    
Create a superuser:

    python manage.py createsuperuser

Run the server:

    python manage.py runserver


You can now open your browser and point it to http://localhost:8000/core

Done! :)