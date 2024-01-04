from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

UserModel = get_user_model()


def validate_registration(data):
    """Validate registration."""
    email = data["email"].strip()
    data["password"].strip()

    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError("Choose another email.")
    try:
        validate_password(data["password"])
    except ValidationError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    return data


def validate_email_present(data):
    """Validate email."""
    email = data["email"].strip()
    if not email:
        raise ValidationError("An email is required.")
    return True


def validate_password_present(data):
    """Validate password."""
    password = data["password"].strip()
    if not password:
        raise ValidationError("A password is required.")
    return True
