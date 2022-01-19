from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import Order, Staff


class StaffViewAPI(generics.ListCreateAPIView):
    """
    Definition of the API for creating and list a Staff object
    """

    queryset = Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = (IsAuthenticated,)


class StaffViewRetrieveAPI(generics.RetrieveUpdateAPIView):
    """
    Definition of the API for retrieve and update a staff object
    """

    queryset = Staff.objects.all()
    serializer_class = serializers.StaffSerializer
    permission_classes = (IsAuthenticated,)


class OrderRetrieveViewAPI(generics.RetrieveUpdateAPIView):
    """
    Definition of the API for retrieve and update a Order object
    """

    lookup_field = "uuid"
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = ()


class OrderListViewAPI(generics.ListAPIView):
    """
    Definition of the API for list a order object
    """

    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (IsAuthenticated,)
