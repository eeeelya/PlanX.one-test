from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from category.models import Category


class Transaction(models.Model):
    amount = models.DecimalField(
        default=0, max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00)]
    )
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    organization = models.CharField(default="", max_length=100)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.category} | {self.amount}"
