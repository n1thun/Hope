from rest_framework import serializers
from api.models import Foreclosure

class ForeclosureSerializer(serializers.Serializer):
    defendant = serializers.CharField()
    address = serializers.CharField(max_length=512)
    sale_date = serializers.DateField()
    zip = serializers.CharField(max_length=11)
    city = serializers.CharField(max_length=128)
    deed_of_trust_amount = serializers.FloatField()
    create_date = serializers.DateField()

    def create(self, validated_data):
        """
        Create and return a new `Foreclosure` instance, given the validated data.
        """
        return Foreclosure.objects.create(**validated_data)

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=512)
    address = serializers.CharField(max_length=512)
    zip = serializers.CharField(max_length=11)
    city = serializers.CharField(max_length=128)
    age = serializers.IntegerField()
    date_of_birth = serializers.DateField()
    in_continuum_of_care = serializers.BooleanField()
    in_shelter = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        """
        return Foreclosure.objects.create(**validated_data)