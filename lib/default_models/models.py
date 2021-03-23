from django.db import models


# Create your models here.


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10)
    is_default = models.BooleanField(default=False)

    class Meta:
        abstract = True
