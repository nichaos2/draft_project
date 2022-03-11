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

## API Documentation with drf-yasg - This is the best
Thi library has both swagger and redoc and also recovers nested api urls
1. install drf-yasg
2. add it in the settings
3. add the [code](https://github.com/axnsan12/drf-yasg/#quickstart) in the url.py
(do not forget to import the *re_path*)
```python
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

drf_yasg_urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```
4. no templates needed
