# ------- REST
from rest_framework import serializers

# ------ models
from .models import Menu, Product
from backend_test.staff.models import Order, Staff
from .tasks import send_slack_message

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
		products = []
		orders = []
		for product_data in products_data:
			products.append(Product(**product_data, menu=menu))
		Product.objects.bulk_create(products)
		staffs = Staff.objects.all().distinct('email')
		for staff in staffs:
			order = Order.objects.create(staff=staff, menu=menu)
			send_slack_message.delay(order=order.id)
		return menu
