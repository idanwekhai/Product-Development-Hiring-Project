from django.db import models
from field_types.models import FieldType
# Create your models here.


class Field(models.Model):
    """Defines all types of fileds"""
    field_type = models.ForeignKey(FieldType, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=260, null=True)
    required = models.NullBooleanField()

    def __str__(self):
        return self.name
