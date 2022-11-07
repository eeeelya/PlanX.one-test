from django.db import models
from django.core.validators import MinValueValidator

from core.abstract_models import SpecialInformation
from user.models import User


class Category(SpecialInformation):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=50)
    total_amount = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)]
    )

    def __str__(self):
        return f"{self.user} | {self.name}"
