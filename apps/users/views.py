
from django.shortcuts import render
from .serializers import UserSerializer, VerificationSerializer
from rest_framework import viewsets
from .models import CustomUser, Verification
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class VerificationViewset(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer
    permission_classes = [IsAuthenticated]
