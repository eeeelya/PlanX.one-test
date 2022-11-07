from django.db import models
from django.utils import timezone


class SpecialInformation(models.Model):
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
