from rest_framework import serializers

from backend_test.menu.models import Product

from .models import Order, Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (
            "id",
            "full_name",
            "email",
            "slack_user",
        )
        read_only_fields = ("id",)


class ProductSlugRelatedField(serializers.SlugRelatedField):
    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(menu=self.root.instance.menu)
        return queryset


class OrderSerializer(serializers.ModelSerializer):
    staff = serializers.SlugRelatedField(slug_field="full_name", read_only=True)
    menu = serializers.SlugRelatedField(slug_field="show_text", read_only=True)
    product = ProductSlugRelatedField(slug_field="description", queryset=Product.objects.all())

    class Meta:
        model = Order
        fields = (
            "staff",
            "menu",
            "product",
            "customizations",
        )
