from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    custom = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
