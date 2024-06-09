from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generic
from . serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.

class CreateUserView(generic.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = User
    permission_class = [AllowAny]
