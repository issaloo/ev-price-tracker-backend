from django.urls import path

from .views import GetEvPriceMainView, GetGraphModelDetailView

urlpatterns = [
    path("main/", GetEvPriceMainView),
    path("graph/<str:pk>", GetGraphModelDetailView),
]
