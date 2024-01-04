from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    # ChangeUserView,
    LoginUserView,
    LogoutUserView,
    RegisterUserView,
    ViewUserView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginUserView, name="login"),
    path("logout/", LogoutUserView, name="logout"),
    path("register/", RegisterUserView, name="register"),
    path("view/", ViewUserView, name="view"),
    # path("change/", ChangeUserView, name="change"),
]
