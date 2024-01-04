from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import LoginUserSerializer, RegisterUserSerializer, UserSerializer
from .validations import (
    validate_email_present,
    validate_password_present,
    validate_registration,
)


class RegisterUser(APIView):

    """Register user.

    Args:
    ----
        APIView (class): DRF API View
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        """Post User Registration Data."""
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

    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        """Post Login Data."""
        data = request.data
        assert validate_email_present(data)
        assert validate_password_present(data)
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

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        """Post Logout."""
        logout(request)
        return Response(status=status.HTTP_200_OK)


LogoutUserView = LogoutUser.as_view()


class ViewUser(APIView):

    """View user.

    Args:
    ----
        APIView (class): DRF API View
    """

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """Get User Data."""
        serializer = UserSerializer(request.user)
        return Response({"user": serializer.data}, status=status.HTTP_200_OK)


ViewUserView = ViewUser.as_view()


# class ChangeUser(APIView):

#     """Change user information.

#     Args:
#     ----
#         APIView (class): DRF API View
#     """

#     # TODO: update with
#     permission_classes = (permissions.IsAuthenticated,)
#     authentication_classes = SessionAuthentication  # TODO: remove this

#     def post(self, request):
#         data = request.data
#         # TODO: need to type in password? or nah,
#         # for each field, assert validate_
#         # if data contains
#         assert validate_password(data)
#         # serializer = LoginUserSerializer(data=data)
#         Change
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.check_user(data)
#             login(request, user)
#             return Response(serializer.data, status=status.HTTP_200_OK)


# ChangeUserView = ChangeUser.as_view()
