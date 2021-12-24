from rest_framework import serializers


class PatientSerializer(serializers.Serializer):
    name = serializers.CharField()
    national_code = serializers.CharField()
    user_ptr_id = serializers.IntegerField()
