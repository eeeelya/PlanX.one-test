from datetime import timedelta

from django.db.models import Count
from django.utils import timezone

from category.models import Category
from transaction.models import Transaction


def count_transactions(user):
    return len(
        Transaction.objects.filter(
            created__range=[timezone.now() - timedelta(days=1), timezone.now()],
            category__user=user,
        )
    )


def find_the_most_popular_category(user):
    most_popular_category = (
        Transaction.objects.filter(
            created__range=[timezone.now() - timedelta(days=1), timezone.now()],
            category__user=user,
        )
        .values("category")
        .annotate(count=Count("category"))
        .order_by("-count")
        .first()
    )

    return (
        Category.objects.get(id=most_popular_category["category"]).name,
        most_popular_category["count"],
    )
