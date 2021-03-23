from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from drugs.models import Drugs
from lib.default_models.models import TimeStampModel, Address


# Create your models here.


class User(AbstractBaseUser, TimeStampModel):
    """User model to store user details"""

    USER_TYPES_CHOICE = (
        ('doctor', 'doctor'),
        ('user', 'user'),
        ('pharmacy', 'pharmacy'),
    )
    SEX = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other")
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    user_type = models.CharField(max_length=24, default='user', choices=USER_TYPES_CHOICE)
    sex = models.CharField(max_length=40, choices=SEX)
    age = models.PositiveIntegerField(default=0)
    phone = PhoneNumberField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'age', 'sex', 'user_type']

    def __str__(self):
        return self.email


class UserAddress(Address, TimeStampModel):
    """Allow user to store multiple address"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address_1} {self.address_2} {self.city}"


class Prescription(TimeStampModel):
    """Store User Prescription"""
    symptoms = models.TextField()
    precautions = models.TextField(null=True, blank=True)
    medicines = models.ManyToManyField(Drugs, through="Medicines", related_name="user_medicine")
    prescriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.symptoms


class Medicines(models.Model):
    """Allow user to store multiple medicines given in prescription"""
    drugs = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="user_prescription")

    def __str__(self):
        return self.prescription.symptoms
