# From MyAcm - Plurasite Tutorials Django: Getting Started

### Module 2 - Starting a Django Project

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

### Module 3 - Creating a Simple Web Page

**Creating a Django app**
```
python manage.py startapp website
# The above creates website directory; remove all contents except __init__.py and views.py

# Now edit meeting_planner/settings.py, in INSTALLED_APPS add 'website', line after all others. 
```

### Module 4 - Setting up a Data Model

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
    Register models with the Admin site (in admin.py)
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

**Adding Room**
```
1.) Add class Room(models.Model): in models.py
2.) python manage.py makemigrations, cancel due to conflicts
3.) Delete numbered files in migrations directory
4.) Delete the database file
5.) python manage.py makemigrations
6.) python manage.py migrate

# Also need to recreate the superuser
python manage.py createsuperuser

# The meeting page now includes a link to add a room.

```

### Module 5 - Combining Model, View & Template
The Model-Template-View pattern (a.k.a. Model View Controller)   

|   -----             |   ------          |  ------         |
| **Model**           |  **Template**     | **View**        |
|   -----             |   ------          | -------         |
| **Data**            | **Presentation**  | **Behavior**    |
| Mapped to DB tables | Generates HTML    | Python function |
|                     |                   | Mapped to URL   |

Add Templates   
Make components work together
* Call model from view
* Call template from view
* View parameters in URLs
* 404 errors

**A Template for the Welcome Page**

Template   
* Generate HTML   
* Call template from view   
* Pass data from view to template   

```
          v---In this case, App name is website
1.) Add website/templates/website/welcome.html
2.) In views.py, change welcome function to 
    return render(request, "website/welcome.html")

    Home on web browser now shows welcome.html created above.
    ```

**A Template for the Welcome Page**

Template Variable: {{message}}

Add to welcome.html
```
<p>
    {{message}}
</p>
```

And change views.py welcome function to:
```
return render(request, "website/welcome.html",
    {"message": "This data was sent from the view to the template"})
```

**A Djanto Template Example**
```
<html><head><title>{{name}}'s page</title></head>
<body>
    <h1>Hi, I'm {{name}}!</h1>
    I'm {{age}} years old.
</body>
</html>

{{var}} looks up var in the template context
Other text is copied to HTML output
This allows creation of dynamic HTML pages
```

**Calling a Template**
```
def home(request):
    return render(request, "website/welcome.html",
        {'name: "bob", 'age': 35})

render: pass request and name of template file
Third argument: dictionary with data passed to the template
Templates must be in directory /templates inside app 
Don't forget the return keyword
```

**Completing the MTV Pattern**

Template   
* Retrieve model data 
* Display it using a template

Meeting detail page
* Retrieve meeting object
* Pass it to template
* Take id parameter from URL
* 404 error when not found

**URLs and Link Building**
Added new template: website/templates/meetings/detail.html
urls.py - added path('meetings/<int:id>', detail),


**Returning a 404 Error**

```
```


**Review**
|   -----               |   ------             |  ------                             |
| **Web Browser**       |                      | **Server**                          |
|   -----               |   ------             | -------                             |
|                       |                      |                                     |
|                       | HTTP GET /meetings/1 |                                     |
| 127.0.0.1/meetings/1  | -------------------> | #Find mapping in urls.py            |
|                       |                      | path('meetings/<int:id>', detail)   |
|                       |                      |                |                    |
|                       |                      |                V                    |
| Meetings with ...     |                      | def detail(request,id):             |
| On February 5th       | <------------------- |   m = get_object_or_404(_)          |
| Starting at 11:00     |                      |   |                |  ^             |
| In conference room    |                      |   V                V  |             |
|                       |                      |  HTML            Database           |

**Retrieving Model Data**
* Model classes have a .objects attribute that let you retrieve data

* Get all objects
meetings = Meeting.objects.all()

* Get object count
num_meetings = Meetings.objects.count()

* Get a specific object
Meeting = Meeting.objects.get(pk=5)

* Get or 404
```
from django.shortcuts import get_object_or_404
from .models import Meeting

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
```

* Parameters in URLs
<int:x> will match a number in the url
This number will be assigned to the view parameter x

For example, /example/5 : x will be 5
```
urlpatterns = [
    path('/example/<int:x>', my_view)
]
```

### Module 6 - URLs & Link Binding 

URLs
* Link building
* Named URL mappings
* URLs & apps
* For loops in templates

Review of Project file structure -> See DjangoFileStructure.txt

Link Building
* Named URLs
* For loop in template

Homework Assignment
Adding views for Rooms
    Required:
    View          -> meeting_planner/website/views.py
    URL mapping   -> meeting_planner/meeting_planner/urls.py
    Template      -> meeting_planner/meetings/templates/meetings/room_list.html (in example code)
                  -> meeting_planner/website/templates/meetings/room_list.html (in mine)

URL mappings best practice 
    App has its own urls.py
    App prefix in main urls.py
    Include app urls in main urls

### Module 7 - Templates, Styling & Static Content

Add styling: CSS (Cascading Style Sheets)
Add styles to the whole site
    Template inheritance
    Makes HTML cleaner

    CSS Templates go in website/static/website
    Images go in the same location

Template Inheritance
    
### Module 8 - Adding User Interaction with Modelforms

Add Meetings
Template: HTML forms
    Generated by ModelForm
View
    Validate input
    Create & sae new meeting
    Redirect after form submit

Forms & Security
    
Demo
    Adding meetings
    Form Template
    ModelForm
    View for Processing Form Data
        Validate
        Save
        Redirect

Understanding the Program Flor for Processing a Form
Forms: General Flow
    1.) Show the Form
       HTML with form elements
       Generated by ModelForm
       HTTP GET
       
    2.) Submit Form Data
        User clicks submit
        HTTP POST
        Validation

    3.) Redirect
        If form validates correctly: show result page
        Otherwise: show form again

Processing User Input 
    See meetings/views.py

A Note About Validation and Security
    The browser has some validation rules, but always validate in your code too.

Customizing Form fields and Validation

    Issues with form:
        Calendar did not work 'date'
        duration line syntax not accepted by django server



 




