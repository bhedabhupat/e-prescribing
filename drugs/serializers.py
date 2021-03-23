from rest_framework import serializers

from drugs.models import Drugs


class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = "__all__"
