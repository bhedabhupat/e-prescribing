from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from drugs.models import Drugs
from lib.default_models.models import TimeStampModel, Address
from user_profile.models import User


# Create your models here.


class Pharmacy(TimeStampModel):
    """Store Pharmacy Details"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drugs = models.ManyToManyField(Drugs)
    website = models.URLField()
    name = models.CharField(max_length=50)
    phone = PhoneNumberField(null=False, blank=False)

    def __str__(self):
        return self.name


class PharmacyAddress(Address, TimeStampModel):
    """Allow pharmacy to store multiple address"""

    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address_1} {self.address_2} {self.city}"
