# api/serializers.py

from rest_framework import serializers
from .models import UVI

class UVISerializer(serializers.ModelSerializer):
    class Meta:
        model = UVI
        fields = '__all__'
