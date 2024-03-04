from django.shortcuts import render
from .serializers import UserSerializer, VerificationSerializer
from rest_framework import viewsets
from .models import User, Verification

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VerificationViewset(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer

