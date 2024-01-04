from django.urls import path

from .views import GetEvPriceMainView, GetGraphModelDetailView

urlpatterns = [
    path("main/", GetEvPriceMainView, name="landing_data"),
    path("graph/<str:pk>", GetGraphModelDetailView, name="graph_data"),
]
