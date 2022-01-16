# ------- REST
from rest_framework import serializers

# ------ models
from .models import Staff, Order


class StaffSerializer(serializers.ModelSerializer):
	class Meta:
		model = Staff
		fields = ('full_name', 'email', 'slack_user',)


class OrderSerializer(serializers.ModelSerializer):
	staff = serializers.SlugRelatedField(
		slug_field='full_name',
		read_only=True
	)

	class Meta:
		model = Order
		fields = ('staff', 'menu', 'customizations',)