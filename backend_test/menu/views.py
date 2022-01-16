# Django
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings

# Rest framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework import generics

# Models
from .models import Menu, Product
# Serializers
from . import serializers


class MenuViewAPI(generics.ListCreateAPIView):
	"""
	Definición de api de creación de tiquetes por medio de web propia
	"""
	queryset = Menu.objects.all()
	serializer_class = serializers.MenuSerializer
	permission_classes = (IsAuthenticated, )