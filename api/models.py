from __future__ import unicode_literals

from django.db import models

class Foreclosure(models.Model):
    defendant = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    saleDate = models.DateField()