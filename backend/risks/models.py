from django.db import models
from risk_types.models import RiskType

# Create your models here.


class Risk(models.Model):
    """Defines all types of risks"""
    risk_type = models.ForeignKey(RiskType, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=260, null=False)

    def __str__(self):
        return self.name
