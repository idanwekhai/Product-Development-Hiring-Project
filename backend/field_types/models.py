from django.db import models

# Create your models here.


class FieldType(models.Model):
    """"Defines the field types"""
    name = models.CharField(max_length=120, null=False)
    description = models.CharField(max_length=260, null=True)

    def __str__(self):
        return self.name
