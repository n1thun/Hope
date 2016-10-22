from __future__ import unicode_literals

from django.db import models

class Foreclosure(models.Model):
    defendant = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    saleDate = models.DateField()
    zip = models.CharField(max_length=6)
    contact = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    deedOfTrustAmount = models.DecimalField()
    createDate = models.DateField()