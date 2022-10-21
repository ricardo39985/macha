from unicodedata import name
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Room(models.Model):
    name = models.CharField()
    description = models.TextField(null=True, blank=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
