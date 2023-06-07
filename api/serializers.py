# api/serializers.py

from rest_framework import serializers
from .models import UVI

class UVISerializer(serializers.ModelSerializer):
    class Meta:
        model = UVI
        fields = '__all__'


        
'''
from rest_framework import serializers
from .models import UVI


class UVISerializer(serializers.ModelSerializer):
    UVI = serializers.ListField(child=serializers.IntegerField())
    areaNo = serializers.IntegerField()
    
    def create(self, validated_data):
        return UVI.objects.create(**validated_data)


class UVISerializer(serializers.ModelSerializer):
    class Meta:
        model = UVI
        fields = '__all__'
'''