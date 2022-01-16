# ------- REST
from rest_framework import serializers

# ------ models
from .models import Menu, Product


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('description',)


class MenuSerializer(serializers.ModelSerializer):
	products = ProductSerializer(many=True, required=True, write_only=True)

	class Meta:
		model = Menu
		fields = ('date', 'show_text', 'products')

	def create(self, validated_data):
		products_data = validated_data.pop('products')
		menu = Menu.objects.create(**validated_data)
		for product_data in products_data:
			Product.objects.create(menu=menu, **product_data)
		return menu
