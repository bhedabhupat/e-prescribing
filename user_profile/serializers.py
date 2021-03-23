from rest_framework import serializers

from user_profile.models import User, Prescription, UserAddress


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    address = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("phone", "password", "first_name", "last_name", "email", "user_type", "sex", "age", "address")

    def get_address(self, obj):
        obj_list = UserAddress.objects.filter(user=obj)
        if obj_list.exists():
            return UserAddressSerializer(obj_list, many=True).data
        else:
            return None


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"
