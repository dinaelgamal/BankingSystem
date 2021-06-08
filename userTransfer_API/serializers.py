from rest_framework import serializers
from .models import transactions

class userTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model =transactions
        fields = '__all__'