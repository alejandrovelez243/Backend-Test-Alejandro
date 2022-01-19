# ------- REST
from rest_framework import serializers

from backend_test.staff.models import Order, Staff

# ------ models
from .models import Menu, Product


class ProductSerializer(serializers.ModelSerializer):
    menu = serializers.SlugRelatedField(slug_field="show_text", read_only=True)

    class Meta:
        model = Product
        fields = ("id", "description", "menu")
        read_only_fields = ("id", "menu")


class MenuSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, required=True, write_only=True)

    class Meta:
        model = Menu
        fields = ("id", "date", "show_text", "products")
        read_only_fields = ("id",)

    def create(self, validated_data):
        products_data = validated_data.pop("products")
        menu = Menu.objects.create(**validated_data)
        products = []
        orders = []
        for product_data in products_data:
            products.append(Product(**product_data, menu=menu))
        Product.objects.bulk_create(products)
        staffs = Staff.objects.all().distinct("email")
        for staff in staffs:
            orders.append(Order(staff=staff, menu=menu))
        Order.objects.bulk_create(orders)
        return menu


class MenuUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            "id",
            "date",
            "show_text",
        )
        read_only_fields = ("id",)
