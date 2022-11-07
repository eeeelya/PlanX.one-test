from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
