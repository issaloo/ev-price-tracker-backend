from django.urls import path

from . import views

urlpatterns = [
    path("", views.GetEvPriceMain.as_view()),
]
