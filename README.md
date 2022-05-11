BASE SET UP

Python -m pip install pipenv // Install pipenv
mkdir 'name'
cd name
Python -m pipenv install django
Python -m django-admin startproject 'name' . // Create a project in the current directory
python manage.py runserver  // start the development server

ACTIVATE VIRTUAL ENVIRONMENT IN VSCODE

python -m pipenv --venv  // get the python interpreter in the virtual environment (run from the directory above)
Go to view - command palette - python select interpreter and choose the interpreter in the virtual environment.

CREATE AN APP

python manage.py startapp 'name' // create an app
register app in settings > INSTALLED APPS

INSTALL DJANGO DEBUG TOOLBAR

pipenv install django-debug-toolbar
read docs for further steps

MIGRATIONS

python manage.py makemigrations
python manage.pyt migrate

CREATE SUPER USER ADMIN PANEL

python manage.py createsuperuser

DJANGO REST FRAMEWORK

pipenv install djangorestframework

DJANGO FILTER

pipenv install django-filter

DJOSER

pipenv install djoser
pipenv install djangorestframework_simplejwt


