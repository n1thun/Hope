from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    zip = models.CharField(max_length=11)
    city = models.CharField(max_length=128)
    age = models.IntegerField()
    dob = models.DateField()
    coc = models.BooleanField()
    shelter_status = models.BooleanField()
    
    def __str__(self):
        return "{}".format(self.name)

class Foreclosure(models.Model):
    defendant = models.ForeignKey('Person', on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    sale_date = models.DateField()
    zip = models.CharField(max_length=11)
    city = models.CharField(max_length=128)
    deed_of_trust_amount = models.DecimalField()
    create_date = models.DateField()

    def __str__(self):
        return "{} forclosed on {}".format(self.defendent, self.create_date)

class ForclosureStatusHistory(models.Model):
    foreclosure = models.ForeignKey('Foreclosure', on_delete=models.CASCADE)
    status = models.CharField(max_length=512)
    date = models.DateField()

    def __str__(self):
        return "{}".format(self.status)
