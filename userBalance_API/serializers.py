from rest_framework import serializers
from .models import userInfo

class userBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model =userInfo
        fields = '__all__'