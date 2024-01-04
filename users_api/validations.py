from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

UserModel = get_user_model()


def validate_registration(data):
    """Validate registration."""
    email = data["email"].strip()
    password = data["password"].strip()

    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError("Choose another email.")
    if not password or len(password) < 8:  # TODO: update password validation here
        raise ValidationError("Choose another password, minimum 8 characters")
    return data


def validate_email(data):
    """Validate email."""
    email = data["email"].strip()
    if not email:
        raise ValidationError("An email is required.")
    return True


def validate_password(data):
    """Validate password."""
    password = data["password"].strip()
    if not password:
        raise ValidationError("A password is required.")
    return True
