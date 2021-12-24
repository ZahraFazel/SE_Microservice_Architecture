from abc import ABC
from rest_framework import serializers


class PrescriptionSerializer(serializers.Serializer, ABC):
    doctor_id = serializers.IntegerField()
    patient_id = serializers.IntegerField()
    drugs = serializers.CharField()
