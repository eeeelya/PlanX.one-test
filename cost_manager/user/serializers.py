from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User, UserCategories
from category.models import Category


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)
    confirmation_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "confirmation_password",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirmation_password"]:
            raise serializers.ValidationError({"detail": "Passwords don't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        categories = Category.objects.filter(custom=False)
        for category in categories:
            UserCategories.objects.create(user=user, category=category)

        return user


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "balance",
            "categories",
            "transactions",
        )
        read_only_fields = ("balance", )


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }
