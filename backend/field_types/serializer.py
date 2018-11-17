from rest_framework import serializers
from .models import FieldType


class FieldTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = FieldType
		fields = '__all__'