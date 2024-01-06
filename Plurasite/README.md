# From MyAcm - Plurasite Tutorials Django: Getting Started

### Unit 2 - Starting a Django Project

**Introducting Django**
```
Django Reinhardt - Jazz Guitar Player
```

**What you should already know**
```
It's Python!
Know how to install python packages

Web Development
HTML, CSS, HTTP

Databases & Basic concepts

Software Requirements
Any operating system: Linux, Mac OS, Windows
Python 3.6 or later (Latest version, or 3.8 recommended)

Editor with Python support (recommended Pycharm, Community Edition)
```

**Project Overview**
```
Tiny Meeting Planner Application
```

**Installing Django**
```
Create New Project ~/PycharmProjects/django_getting_started
    In Pycharm, a virtual environment is created automatically
    If using another editor, watch "Managing Python Packages & Virtual Environments" course

Installing Django
    Use terminal in Virtual Environment associated with the project created above.

    python -m pip install django
    # Related course working files can be cloned:
    git clone https://github.com/codesensei-courses/django_getting_started
```

**Starting a Project**
```
Using terminal in Virtual Environment
    django-admin startproject meeting_planner
    # Command above creates meeting_planner directory with manage.py, move into that directory
    python manage.py runserver
    # A warning is displayed that can be ignored for now.
    # The URL should allow opening the web page.

-->> BEST PRACTICE - Always install packages inside a Virtual Environment <<--
```

### Unit 3 - Creating a Simple Web Page

**Creating a Django app**
```
python manage.py startapp website
# The above creates website directory; remove all contents except __init__.py and views.py

# Now edit meeting_planner/settings.py, in INSTALLED_APPS add 'website', line after all others. 
```

### Unit 4 - Setting up a Data Model

**Introducing Models and Migrations**
```
Data Model
    Create Django model classes
    Create and run migrations
    Edit data with admin interface
```

|   -----                            |   ------                             | 
| Models                             |  Migrations                          |
|   -----                            |   ------                             | 
| Python classes                     | Python scripts                       |
| Mapped to DB tables                | Keep DB structure in sync with code  |
| Each object is a row in the table  | Auto generated (but not always)      |


**Running Initial Migrations**
```
python manage.py showmigrations     # Shows pending migrations
python manage.py migrate            # Performs migrations

sudo dnf -y install sqlite
python manage.py dbshell             # starts sqlite shell

.tables     # shows tables
select * from django_migrations      # 

.exit                                # Exits sqlite shell
```
**Creating a Model Class**
```
python manage.py startapp meetings
```

**Creating and Running Migrations**
```
python manage.py makemigrations

Creates 0001_initial.py

python manage.py sqlmigrate meetings 0001
python manage.py migrate

python manage.py dbshell
.tables                     # <- should show meetings_meetings table exists
```

**Combining Model, View, and Template**
```
# Admin Interface
    Create and edit model data
    Register model with admin site
    Configure superuser

Start server, then URL/admin will show login page.

Create user account:
   python manage.py createsuperuser
   User: developer
   Email ....
   Password CS00

Restart server & login

Can now click on Meetings -> Add

For more info: Search for -> django model fields
```

**Review**
```
# Migration Workflow

IMPORTANT: make sure your app is in INSTALLED_APPS 

    Step 1: Change model code
    Step 2: Generate migration script (and check it!)

    python manage.py makemigrations

    # optional Show migrations
    python manage.py showmigrations

    Step 3: Run migrations
    python manage.py migrate

# Prerequisite
    Register models with the Admin site (in adin.py)
    If account hasn't been created yet:
        python mange.py createsuperuser
```

**Bring it all together**
```
# Add fields to models
In models.py, add fields to table
    start_time = models.TimeField()
    duration = models.IntergerField()

python manage.py makemigrations
    Receive an error concerning what default values to assign to existing rows.  Press 2 to quit.

    Add default values to models.py
    python manage.py makemigrations
    python manage.py migrate




```












```

