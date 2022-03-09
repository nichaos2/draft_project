# First turorial from the documentation

(revision on django - just copy paste)

## pipenv

if pipenv does not work do this first
export PATH=$PATH:/home/nioannou/.local/bin/


## commands

```
django-admin startproject <the_project>
python manage.py runserver
python manage.py startapp <the_app>
python manage.py makemigrations <the_app>
python manage.py shell
python manage.py createsuperuser
```

## use the shell

>>> from polls.models import Choice, Question
>>> from django.utils import timezone
>>> Question.objects.all()
etc...

## testing

- conventional unit tests for functions -> could I use pytest
and 
- unit tests for views, what response they get

### coverage

```
coverage run --source='.' manage.py test <myapp>
```
This runs your tests and collects coverage data of the executed files in your project. You can see a report of this data by typing following command:
```
coverage report
```