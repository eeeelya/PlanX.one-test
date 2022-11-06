from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

from category.models import Category
from transaction.models import Transaction


class User(AbstractUser):
    balance = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)]
    )
    categories = models.ManyToManyField(Category, through="UserCategories")
    transactions = models.ManyToManyField(Transaction, through="UserTransactions")


class UserCategories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_amount = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)]
    )


class UserTransactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
