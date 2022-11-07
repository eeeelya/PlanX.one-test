from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.utils import timezone
from django.db.models import F

from transaction.models import Transaction
from category.models import Category
from user.models import User


class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = Transaction
        fields = (
            "amount",
            "description",
            "organization",
            "category",
            "category_name",
        )
        read_only_fields = ("category",)
        extra_kwargs = {
            "amount": {"required": True},
        }

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context["request"].user.id)

        category = get_object_or_404(
            Category,
            user__id=user.id,
            name=validated_data["category_name"],
        )

        transaction = Transaction.objects.create(
            category=category,
            amount=validated_data["amount"],
            description=validated_data["description"],
            organization=validated_data["organization"],
        )

        category.total_amount = F("total_amount") + validated_data["amount"]
        category.save()

        if validated_data["category_name"] == "Зарплата":
            user.balance = F("balance") + validated_data["amount"]
        else:
            user.balance = F("balance") + validated_data["amount"]

        user.save()

        return transaction

    def update(self, instance, validated_data):
        instance.updated = timezone.now()

        return super().update(instance, validated_data)
