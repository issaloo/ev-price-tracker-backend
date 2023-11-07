from django.contrib import admin
from django.urls import include, path

handler400 = "rest_framework.exceptions.bad_request"

urlpatterns = [path("admin/", admin.site.urls), path("api/", include("api.urls"))]
