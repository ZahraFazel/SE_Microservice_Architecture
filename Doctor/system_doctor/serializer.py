from abc import ABCMeta, ABC

from rest_framework import serializers


class DoctorSerializer(serializers.Serializer, ABC):
    name = serializers.CharField()
    national_code = serializers.CharField()
    user_ptr_id = serializers.IntegerField()
