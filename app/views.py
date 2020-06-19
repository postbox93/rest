from django.shortcuts import render
from .serializers import EmployeeSerializer
from django.contrib.auth.models import User


from rest_framework import viewsets
# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = EmployeeSerializer