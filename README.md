# django-tutorial   
Based on tutorials from [Django Project Documentation](https://docs.djangoproject.com/en/3.2/howto/static-files/)

## Installation notes  
Currently using Rocky 8 for an operating system, which ships with Python 3.6, therefore Django 3.2 is the most recent version than can be used.    

```
pip3 install --user Django==3.2
mkdir repositories
mkdir repositories/django-tutorial
cd repositories/django-tutorial
django-admin startproject mysite
cd mysite/

# In another shell window
python3 manage.py runserver 8080

# NOTE that Firefox would not respond to http://127.0.0.1:8080
# http://localhost:8080  <<== This worked.

```

