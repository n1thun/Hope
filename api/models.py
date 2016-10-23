from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    zip = models.CharField(max_length=11)
    city = models.CharField(max_length=128)
    age = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(null=True)
    in_continuum_of_care = models.BooleanField(default=False)
    in_shelter = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}".format(self.name)

class Foreclosure(models.Model):
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    sale_date = models.DateField(null=True)
    zip = models.CharField(max_length=11)
    city = models.CharField(max_length=128, blank=True)
    deed_of_trust_amount = models.CharField(max_length=64, null=True, blank=True)
    create_date = models.DateField(null=True)

    def __str__(self):
        return "{} forclosed on {}".format(self.name, self.create_date)

class ForclosureStatusHistory(models.Model):
    foreclosure = models.ForeignKey('Foreclosure', on_delete=models.CASCADE)
    status = models.CharField(max_length=512)
    date = models.DateField()

    def __str__(self):
        return "{}".format(self.status)
