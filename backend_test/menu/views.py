from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import serializers
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
