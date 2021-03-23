from django.db import models

from lib.default_models.models import TimeStampModel


# Create your models here.


class Drugs(TimeStampModel):
    """ Drugs Models to store Medicines"""

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    benefit = models.TextField(null=True, blank=True)
    side_effect = models.TextField(null=True, blank=True)
    advice = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
