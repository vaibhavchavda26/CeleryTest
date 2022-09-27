from rest_framework import serializers
from core import models as core_models

class TestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length = 40)
    last_name = serializers.CharField(max_length = 40)
    email = serializers.EmailField(max_length = 40)
    phone_no = serializers.IntegerField()
    address = serializers.CharField(max_length = 100)
