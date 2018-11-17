from django.db import models
from fields.models import Field
from risks.models import Risk
# Create your models here.


class FieldByRisk(models.Model):
	"""Defines the fields by risk"""
	field = models.ForeignKey(Field, null=False, on_delete=models.CASCADE)
	risk = models.ForeignKey(Risk, null=False, on_delete=models.CASCADE)
	value = modles.CharField(max_length=120, null=False)

	def __str__(self):
		return self.value