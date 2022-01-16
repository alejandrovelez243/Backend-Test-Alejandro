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
from .models import Staff, Order
# Serializers
from . import serializers


class StaffViewAPI(generics.ListCreateAPIView):
	"""
	Definición de api de creación de tiquetes por medio de web propia
	"""
	queryset = Staff.objects.all()
	serializer_class = serializers.StaffSerializer
	permission_classes = (IsAuthenticated, )


class OrderViewAPI(generics.RetrieveUpdateAPIView):
	"""
	Definición de api de creación de tiquetes por medio de web propia
	"""
	lookup_field = "uuid"
	queryset = Order.objects.all()
	serializer_class = serializers.OrderSerializer
	permission_classes = ()