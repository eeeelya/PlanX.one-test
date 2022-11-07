from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User
from category.models import Category


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)
    confirmation_password = serializers.CharField(write_only=True, required=True)

    DEFAULT_CATEGORIES = (
        "Забота о себе",
        "Зарплата",
        "Здоровье и фитнес",
        "Кафе и рестораны",
        "Машина",
        "Образование",
        "Отдых и развлечения",
        "Платежи, комиссии",
        "Покупки: одежда, техника",
        "Продукты",
        "Проезд",
    )

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

        for category in self.DEFAULT_CATEGORIES:
            Category.objects.create(user=user, name=category)

        user.save()

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
        )


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}}
