from django.db import models

# Create your models here.
class RiskType(models.Model):
	"""Defines the risk type"""
	name = models.CharField(max_length=120, null=False)
	description = models.CharField(max_length=260, null=True)

	def __str__(self):
		return self.name
