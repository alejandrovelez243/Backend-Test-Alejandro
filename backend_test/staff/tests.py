from django.test import Client, RequestFactory, TestCase
from rest_framework.authtoken import views

from backend_test.menu.models import Menu, Product

from .models import Order, Staff, User
from .serializers import OrderSerializer, StaffSerializer
from .views import (
    OrderListViewAPI,
    OrderRetrieveViewAPI,
    StaffViewAPI,
    StaffViewRetrieveAPI,
)

# Create your tests here.


class ApiTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="admin", password="abc1234*")
        staff = Staff.objects.create(
            email="test@hotmail.com", full_name="test", slack_user="@test"
        )
        menu = Menu.objects.create(show_text="Test", date="2022-01-01")
        order = Order.objects.create(menu=menu, staff=staff)

    def test_token(self):
        request = self.factory.post(
            "/api-token-auth/", {"username": "admin", "password": "abc1234*"}
        )
        response = views.obtain_auth_token(request)
        self.assertEqual(response.status_code, 200)

    def test_order_list(self):
        request = self.factory.get("/order/")
        request.user = self.user
        response = OrderListViewAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)
