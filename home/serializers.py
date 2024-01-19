from rest_framework import serializers
from .models import RiskData

class RiskDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskData
        fields = ['name', 'date', 'rate']
