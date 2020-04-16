## ga_project4
GA - Capstone
Project Link: [GitHub grimmana ga_project4](https://github.com/grimmana/ga_project4)

### Project Description:
This application allows users to add and store information about their household possessions.

Features:
- Have two related models.
- Implement Full CRUD throughout the application
- Utilizes user authentication and routes that require login for access.

Technologies used:
Django
GitHub
Python
PostgreSQL
NodeJS
Virtual environments
React

Issues and resolutions: 



### Additional Resources

- [GA Docs: Django models](https://git.generalassemb.ly/jdr-0127/django-models)
- [Django Docs: Models](https://docs.djangoproject.com/en/2.0/topics/db/models/)
- [Django Docs: Models & Databases](https://docs.djangoproject.com/en/2.0/topics/db/)
- [How to Create Django Models](https://www.digitalocean.com/community/tutorials/how-to-create-django-models)
- [Django Docs: Migrations](https://docs.djangoproject.com/en/2.0/topics/migrations/)
- [Django Docs: Writing Database Migrations](https://docs.djangoproject.com/en/2.0/howto/writing-migrations/)
- [Django Docs: Admin](https://docs.djangoproject.com/en/2.1/ref/django-admin/)
- [Django Docs: Providing initial data for models](https://docs.djangoproject.com/en/2.1/howto/initial-data/)
- [Django Extensions](https://github.com/django-extensions/django-extensions)
- [GA Docs: Django views and templates](https://git.generalassemb.ly/jdr-0127/django-views-and-templates)


### Installation Instructions 

# Getting Started
1. Create a new repository on your personal GitHub account 
2. Fork and clone down this repository.


# Set up the Django application
Create a directory for the application on your computer:

```bash
mkdir homi_django
```

Then, `cd` into the `homi_django/` folder you created.

Run the following commands to set up the virtual environment:

```bash
python3 -m pip install virtualenv
python3 -m venv .env
source .env/bin/activate
```

The command `source .env/bin/activate` activates the virtual environment, so remember to activate it each time you work on your project.


Install Django:

```
python3 -m pip install django 
```

If prompted that a more current version of pip is available; go ahead and run the upgrade

```
pip install --upgrade pip
```

Install the library to connect Django to PostgreSQL:

```
python3 -m pip install psycopg2-binary
```		

Start the Django project - 
> For the next command, make sure you include the `.` on the end! This creates the project in the current directory instead of creating a new subfolder.

```sh
django-admin startproject homi_django .
```

Create the app:

```bash
$ django-admin startapp homi
```

> Note: if django-admin doesn't work, you can replace it with
> `python3 manage.py`, assuming `manage.py` is in your current directory.


The application structure looks like this now:
 
- homi_django 
    - .env
    - homi
        - Migrations
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
    - homi_django
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    manage.py
- planning
    project_estimates.md
    project_idea_model.md
    user_stories.md
    wireframe.md    
README.md

====== GIT COMMIT 1 =========

# Database Setup

Using pSQL

Login to `psql`:

```bash
$ psql -d postgres
```

Create a database:

```sql
> CREATE DATABASE homi;
> CREATE USER homiuser WITH PASSWORD 'homi';
> GRANT ALL PRIVILEGES ON DATABASE homi TO homiuser;
> \q
```

Then, in `homi_django/homi_django/settings.py` find the `DATABASES` constant dictionary.
Update it to look like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'homi',
        'USER': 'homiuser',
        'PASSWORD': 'homi',
        'HOST': 'localhost'
    }
}
```
Add the application `homi` to the bottom line of the
 `INSTALLED_APPS` list.

 ```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homi'
]
```

In the terminal run `python3 manage.py runserver` then in the browser navigate to 
`localhost:8000`

You should see a page welcoming you to Django!

========= GIT COMMIT 2 ==========

# Models

In: homi_django/homi/models.py

Create the primary class `Room` with the field `name`, and the default method `def __str__in`: 

Create the secondary class `Item` and then add the default method `def __str__in:


```python
class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.CharField(max_length=100)
    name = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='items')
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serialnumber = models.CharField(max_length=100)
    purchasedate = models.CharField(max_length=100) 
    purchaseprice = models.CharField(max_length=100) 
    warranty = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name
```

# Migrations 

Use the `makemigrations` and `migrate` commands to migrate the new model classes `Room` and `Item` to the database:

```bash
$ python3 manage.py makemigrations
```

Run the next command after all the changes to the models file have been completed:

```bash
$ python3 manage.py migrate
```

Reminder: if you make changes, make them in the models.py file. **NEVER** edit the migration files manually.  


# Initial database Seed using the Admin Console

To use the Django admin dashboard with the built-in CRUD functionality:

Add the following code to the homi_django/homi/admin.py file to register the model classes `Room` and `Item`.

```python
from .models import Room, Item
admin.site.register(Room)
admin.site.register(Item)  
```

Run the `makemigrations` and `migrate` commands again now:

```bash
$ python3 manage.py makemigrations
```

```bash
$ python3 manage.py migrate
```


# Admin Console 

Create a superuser for the application. In the terminal, run:

```bash
$ python3 manage.py createsuperuser
```
Fill in the requested super user information as prompted.


Next, in the browser go to the Admin Console http://localhost:8000/admin/

Manually add the seed data.

Return to VScode:

xxxx End using Admin for Seed data


========= GIT COMMIT 3 ==========


# Django Extensions - 

Install additional debugging functionality to Django.

```sh
$ python3 -m pip install django-extensions
```

Then, in `homi_django/homi_django/settings.py` find the `INSTALLED_APPS` list.
Add `django_extensions` to the bottom of this section.

```py
# part_django/settings.py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'part',
    'jdango_extensions'
]

To get to a python shell, you can now run:

```
$ python3 manage.py shell_plus
```

To exit:

```
quit()
```

For a nicer interface install ipython:

```sh
$ python3 -m pip install ipython
```

Now you can enter it:"

```sh
python3 manage.py shell_plus --ipython
```

========= GIT COMMIT 4 ==========


# Django Views & Templates

# View Functions

Create the Room and Item views in /homi_jdango/homi/views.py: 

```python
# homi_django/homi/views.py
from django.shortcuts import render
from .models import Room, Item

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'homi/room_list.html', {'rooms': rooms})

def item_list(request):
    items = Item_part.objects.all()
    return render(request, 'homi/item_list.html', {'items': items})
```
========= GIT COMMIT 5 ==========
# URLs

Edit /homi_jdango/homi_jdango/urls.py: Add to the first line import - `include` 

```python
# homi_django/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('homi.urls')),
]
```
========= GIT COMMIT 6 ==========
