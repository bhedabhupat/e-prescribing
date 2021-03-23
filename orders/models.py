from django.db import models
from django.db.models.signals import pre_save

from lib.default_models.models import TimeStampModel
from pharmacy.models import Pharmacy
from user_profile.models import User, Prescription, Medicines, UserAddress


# Create your models here.


class Booking(TimeStampModel):
    """Allow user to order medicines using provided prescriptions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    user_prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="prescription")
    amount = models.PositiveIntegerField(default=0)
    delivery_address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email}-{self.amount}"
