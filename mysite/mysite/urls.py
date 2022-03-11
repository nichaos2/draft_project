"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path,re_path

# swagger
# from rest_framework.schemas import get_schema_view
# from django.views.generic import TemplateView

# drf_yasg
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# urlpatterns
urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

# swagger
# swagger_urlpatterns = [
#     # schema for api
#     path(
#         "openapi/",
#         get_schema_view(
#             title="Poll Service",
#             description="API for developers who would love to use our service",
#         ),
#         name="openapi-schema",
#     ),
#     # Route TemplateView to serve Swagger UI template.
#     #   * Provide `extra_context` with view name of `SchemaView`.
#     path(
#         "docs/",
#         TemplateView.as_view(
#             template_name="api_docs.html",
#             extra_context={"schema_url": "openapi-schema"},
#         ),
#         name="swagger-ui",
#     ),
# ]

# urlpatterns += swagger_urlpatterns

# drf_yasg
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
urlpatterns += drf_yasg_urlpatterns