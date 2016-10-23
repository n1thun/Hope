from rest_framework import serializers
from api.models import Foreclosure, Person, ForclosureStatusHistory



class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=512, required=True)
    address = serializers.CharField(max_length=512, required=False)
    zip = serializers.CharField(max_length=11, required=False)
    city = serializers.CharField(max_length=128, required=False)
    age = serializers.IntegerField(required=False)
    date_of_birth = serializers.DateField(required=False)
    in_continuum_of_care = serializers.BooleanField(required=False)
    in_shelter = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        """
        return Person.objects.create(**validated_data)


class ForeclosureSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField(max_length=512, required=False)
    sale_date = serializers.CharField(required=False)
    zip = serializers.CharField(max_length=11, required=False)
    city = serializers.CharField(max_length=128, required=False)
    deed_of_trust_amount = serializers.CharField(required=False)
    create_date = serializers.DateField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Foreclosure` instance, given the validated data.
        """
        return Foreclosure.objects.create(**validated_data)

class ForclosureStatusHistorySerializer(serializers.Serializer):
    foreclosure = ForeclosureSerializer(many=True)
    status = serializers.CharField(max_length=512)
    date = serializers.DateField()

    def create(self, validated_data):
        """
        Create and return a new `Person` instance, given the validated data.
        """
        return ForclosureStatusHistory.objects.create(**validated_data)