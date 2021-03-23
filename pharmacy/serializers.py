from rest_framework import serializers

from pharmacy.models import Pharmacy, PharmacyAddress


class PharmacySerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pharmacy
        fields = ("id", "user", "drugs", "website", "name", "phone", "address")

    def get_address(self, obj):
        obj_list = PharmacyAddress.objects.filter(pharmacy=obj)
        if obj_list.exists():
            return PharmacyAddressSerializer(obj_list, many=True).data
        else:
            return None


class PharmacyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyAddress
        fields = "__all__"
