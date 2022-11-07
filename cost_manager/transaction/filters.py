from django_filters import FilterSet, filters

from transaction.models import Transaction


class TransactionFilter(FilterSet):
    class Meta:
        model = Transaction
        fields = ("created", "amount")
