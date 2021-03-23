from rest_framework import serializers

from orders.models import Booking


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
