from re import M
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.industry}"
