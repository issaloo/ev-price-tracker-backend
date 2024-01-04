from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):

    """Custom User for Login, using email as username."""

    username = None
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        """Email as string representation."""
        return self.email
