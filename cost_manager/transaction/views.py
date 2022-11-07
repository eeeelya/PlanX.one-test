from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend

from core.mixins import DeactivateModelMixin
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from transaction.filters import TransactionFilter


class TransactionViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    DeactivateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TransactionSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TransactionFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Transaction.objects.filter(is_active=True)

        return Transaction.objects.filter(category__user=self.request.user, is_active=True)

