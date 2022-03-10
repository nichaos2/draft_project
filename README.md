# First turorial from the documentation

This is the Polls (Questions/Choices) app from the django from documentation.

The purpose is to revise the basics.

Also I added the basics of Rest Django API + swagger

Try to follow this 2+ hours [tutorial](https://www.youtube.com/watch?v=B38aDwUpcFc&ab_channel=ParwizForogh) on youtube 

## pipenv

I use the pipenv to manage the packages

- if pipenv does not work do this first
export PATH=$PATH:/home/nioannou/.local/bin/


## commands

Bqsic commands to start the project
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

## Django Rest Framework

1. pipenv install djangorestframework djangorestframework-jsonapi django-filter
2. add it to settings.py
3. create serializers for the models
4. add the views
5. wire up the API URLs

## API Documentation with swagger and openapi schema

1. install django-rest-swagger pyyaml
2. in the project Confurls add schema (openapi)
3. add swagger url
4. add template in the app/templates folder