from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from category.serializers import CategorySerializer
from category.models import Category
from core.mixins import DeactivateModelMixin


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Category.objects.filter(is_active=True)

        return Category.objects.filter(user=self.request.user, is_active=True)
