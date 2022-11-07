from django_filters import FilterSet, filters

from transaction.models import Transaction


class TransactionFilter(FilterSet):
    created_date = filters.DateFromToRangeFilter(field_name="created")
    created_time = filters.TimeRangeFilter(field_name="created")
    amount_gte = filters.NumberFilter(field_name="amount", lookup_expr="gte")
    amount_lte = filters.NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Transaction
        fields = ("created_date", "created_time", "amount_gte", "amount_lte")
