from celery import shared_task
from django.core.mail import send_mail

from user.models import User
from cost_manager.settings import EMAIL_HOST_USER
from user.statistics import count_transactions, find_the_most_popular_category


@shared_task
def send_statistics():
    active_users = User.objects.filter(is_active=True, is_superuser=False)

    for user in active_users:
        amount_trans = count_transactions(user)
        most_popular_category = find_the_most_popular_category(user)

        send_mail(
            "Daily statistics from Cost Manager.",
            f"Total transactions {amount_trans}\n."
            f"Most popular category - {most_popular_category[0]} with amount {most_popular_category[1]}.",
            EMAIL_HOST_USER,
            [user.email],
        )
