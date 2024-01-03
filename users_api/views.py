from django.contrib.auth import login, logout
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# TODO: missing JWT authentication
from .serializers import LoginUserSerializer, RegisterUserSerializer, UserSerializer
from .validations import (
    validate_email,
    validate_password,
    validate_registration,
)


class RegisterUser(APIView):

    """Register user.

    Args:
    ----
        APIView (class): DRF API View
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        clean_data = validate_registration(request.data)
        serializer = RegisterUserSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


RegisterUserView = RegisterUser.as_view()


class LoginUser(APIView):

    """Login user.

    Args:
    ----
        APIView (class): DRF API View
    """

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)  # TODO: do JWT for this

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


LoginUserView = LoginUser.as_view()


class LogoutUser(APIView):

    """Logout user.

    Args:
    ----
        APIView (class): DRF API View
    """

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


LogoutUserView = LogoutUser.as_view()


class ViewUser(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = SessionAuthentication  # TODO: remove this

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)


ViewUserView = ViewUser.as_view()


class ChangeUser(APIView):

    """Change user information.

    Args:
    ----
        APIView (class): DRF API View
    """

    # TODO: update with
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = SessionAuthentication  # TODO: remove this

    def post(self, request):
        data = request.data
        # TODO: need to type in password? or nah,
        # for each field, assert validate_
        # if data contains
        assert validate_password(data)
        # serializer = LoginUserSerializer(data=data)
        Change
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


ChangeUserView = ChangeUser.as_view()
