from abc import ABC
from rest_framework import serializers


class PatientSerializer(serializers.Serializer, ABC):
    name = serializers.CharField()
    national_code = serializers.CharField()
    user_ptr_id = serializers.IntegerField()
