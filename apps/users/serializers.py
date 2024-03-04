from rest_framework import serializers
from .models import User, Verification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_boss',]


class VerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verification
        fields = '__all__'
