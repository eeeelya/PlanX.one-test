from django.core.validators import MinValueValidator
from django.db import models

from category.models import Category
from core.abstract_models import SpecialInformation


class Transaction(SpecialInformation):
    amount = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)]
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    organization = models.CharField(default="", max_length=100)

    def __str__(self):
        return f"{self.category} | {self.amount}"
