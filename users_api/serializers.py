from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers

UserModel = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):

    """Register User serializer."""

    class Meta:

        """Use UserModel."""

        model = UserModel
        fields = "__all__"

    def create(self, clean_data):
        """Create User and Save to DB."""
        user_obj = UserModel.objects.create_user(email=clean_data["email"], password=clean_data["password"])
        user_obj.first_name = clean_data["first_name"]
        user_obj.last_name = clean_data["last_name"]
        user_obj.save()
        return user_obj


class LoginUserSerializer(serializers.ModelSerializer):

    """Login User serializer."""

    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, clean_data):
        """Authenticate User."""
        user = authenticate(username=clean_data["email"], password=clean_data["password"])
        if not user:
            raise ValidationError("User not found")
        return user


# class ChangeUserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()
#     # how to make it optional
#     # def check_user(self, clean_data):
#     #     user = authenticate(username=clean_data["email"], password=clean_data["password"])
#     #     if not user:
#     #         raise ValidationError("User not found")
#     #     return user


class UserSerializer(serializers.ModelSerializer):

    """View User serializer."""

    class Meta:

        """Use UserModel."""

        model: UserModel
        fields = ["email", "first_name", "last_name"]
