from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    UNSET = -1

    DIVORCED = 2
    MARRIED = 1
    UNMARRIED = 0

    CAUCASIAN = 0
    AFRICANAMERICAN = 1
    HISPANIC = 2
    ASIAN = 3

    MARITAL_STATUS_KEYS = (
        (UNSET, ' '),
        (DIVORCED, 'Divorced'),
        (MARRIED, 'Married'),
        (UNMARRIED, 'Unmarried')
    )

    ETHINICITY_KEYS = (
        (UNSET, ' '),
        (CAUCASIAN, 'caucasian'),
        (AFRICANAMERICAN, 'African American'),
        (HISPANIC, 'Hispanic'),
        (ASIAN, 'Asian')
    )

    name = models.CharField(max_length=128)
    address = models.CharField(max_length=512)
    zip = models.CharField(max_length=11)
    city = models.CharField(max_length=128)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    in_continuum_of_care = models.BooleanField()
    in_shelter = models.BooleanField()
    marital_status_type = models.IntegerField(('Marital status'), choices=MARITAL_STATUS_KEYS, default=UNSET)
    ethinicity_type = models.IntegerField(('Race'), choices=ETHINICITY_KEYS, default=UNSET)
    family_size = models.IntegerField(default=0)
    was_previously_homeless = models.BooleanField(default=False)
    has_prior_criminal_record = models.BooleanField(default=False)
    has_disabilities = models.BooleanField(default=False)
    is_pregnant = models.BooleanField(default=False)
    is_veteran = models.BooleanField(default=False)
    in_employed = models.BooleanField(default=False)
    has_mental_health_issues = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)

#
# class Person_more_details(models.Model):
#     UNSET = -1
#
#     DIVORCED = 2
#     MARRIED = 1
#     UNMARRIED = 0
#
#     CAUCASIAN = 0
#     AFRICANAMERICAN = 1
#     HISPANIC = 2
#     ASIAN = 3
#
#     MARITAL_STATUS_KEYS = (
#         (UNSET, ' '),
#         (DIVORCED, 'Divorced'),
#         (MARRIED, 'Married'),
#         (UNMARRIED, 'Unmarried')
#     )
#
#     ETHINICITY_KEYS = (
#         (UNSET, ' '),
#         (CAUCASIAN, 'caucasian'),
#         (AFRICANAMERICAN, 'African American'),
#         (HISPANIC, 'Hispanic'),
#         (ASIAN, 'Asian')
#     )
#
#     person_link = models.ForeignKey('Person', on_delete=models.CASCADE)
#     marital_status_type = models.IntegerField(('Marital status'), choices=MARITAL_STATUS_KEYS, default=UNSET)
#     ethinicity_type = models.IntegerField(('Race'), choices=ETHINICITY_KEYS, default=UNSET)
#     family_size = models.IntegerField()
#     was_previously_homeless = models.BooleanField()
#     has_prior_criminal_record = models.BooleanField()
#     has_disabilities = models.BooleanField()
#     is_pregnant = models.BooleanField()
#     is_veteran = models.BooleanField()
#     in_employed = models.BooleanField()
#     has_mental_health_issues = models.BooleanField()
#
#
#     def __str__(self):
#         return "Is employed: {}, was veteran {}".format(self.is_veteran, self.in_employed)

class Foreclosure(models.Model):
    defendant = models.ForeignKey('Person', on_delete=models.CASCADE)
    address = models.CharField(max_length=512)
    sale_date = models.DateField()
    zip = models.CharField(max_length=11)
    city = models.CharField(max_length=128)
    deed_of_trust_amount = models.DecimalField(max_digits=12, decimal_places=2)
    create_date = models.DateField()

    def __str__(self):
        return "{} forclosed on {}".format(self.defendent, self.create_date)

class ForclosureStatusHistory(models.Model):
    foreclosure = models.ForeignKey('Foreclosure', on_delete=models.CASCADE)
    status = models.CharField(max_length=512)
    date = models.DateField()

    def __str__(self):
        return "{}".format(self.status)
