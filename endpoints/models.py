from pyexpat import model
from django.db import models

# Create your models here.
class Result(models.Model):
  argument = models.IntegerField()
  result = models.IntegerField(null=True, blank=True)