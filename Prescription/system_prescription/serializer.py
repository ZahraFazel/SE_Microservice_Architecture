from rest_framework import serializers


class PrescriptionSerializer(serializers.Serializer):
    doctor_id = serializers.IntegerField()
    patient_id = serializers.IntegerField()
    drugs = serializers.CharField()
    date = serializers.DateField()
