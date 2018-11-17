from rest_framework import serializers
from .models import RiskType


class RiskTypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = RiskType
        fields = '__all__'