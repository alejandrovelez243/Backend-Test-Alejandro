# Django
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import generics, mixins, viewsets

# Rest framework
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

# Serializers
from . import serializers

# Models
from .models import Menu, Product


class MenuViewAPI(generics.ListCreateAPIView):
    """
    Definition of the API for creating and list a Menu object
    """

    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    permission_classes = (IsAuthenticated,)


class MenuViewRetrieveAPI(generics.RetrieveUpdateAPIView):
    """
    Definition of the API for retrieve and update a Menu object
    """

    queryset = Menu.objects.all()
    serializer_class = serializers.MenuUpdateSerializer
    permission_classes = (IsAuthenticated,)


class ProductViewAPI(generics.ListAPIView):
    """
    Definition of the API for list a Product object
    """

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated,)


class ProductViewRetrieveAPI(generics.RetrieveUpdateAPIView):
    """
    Definition of the API for retrieve and update a Product object
    """

    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = (IsAuthenticated,)
