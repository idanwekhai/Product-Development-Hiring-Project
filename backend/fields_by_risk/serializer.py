from rest_framework import serializers
from .models import FieldByRisk
from risks.serializer import RiskSerializer
from fields.serializer import FieldSerializer


class FieldByRiskSerializer(serializers.ModelSerializer):
    risk = RiskSerializer(read_only=True)
    field = FieldSerializer(read_only=True)

    class Meta:
        model = FieldByRisk
        fields = '__all__'
