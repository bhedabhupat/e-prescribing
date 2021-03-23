from django.contrib import admin
from user_profile.models import User, UserAddress, Prescription, Medicines

admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(Prescription)
admin.site.register(Medicines)
