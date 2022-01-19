from django.test import RequestFactory, TestCase
from rest_framework.authtoken import views

from backend_test.menu.models import Menu

from .models import Order, Staff, User
from .serializers import OrderSerializer, StaffSerializer
from .views import (
    OrderListViewAPI,
    OrderRetrieveViewAPI,
    StaffViewAPI,
    StaffViewRetrieveAPI,
)

# Create your tests here.


class SerializersTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="admin", password="abc1234*")
        self.staff = Staff.objects.create(
            email="test@hotmail.com", full_name="test", slack_user="@test"
        )
        menu = Menu.objects.create(show_text="Test", date="2022-01-01")
        self.order = Order.objects.create(menu=menu, staff=self.staff)

    def test_order_serializer(self):
        serializer = OrderSerializer(self.order)
        self.assertEqual(serializer.data.get("menu"), "Test")

    def test_staf_serializer(self):
        serializer = StaffSerializer(self.staff)
        self.assertEqual(serializer.data.get("full_name"), "test")


class ApiTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="admin", password="abc1234*")
        self.staff = Staff.objects.create(
            email="test@hotmail.com", full_name="test", slack_user="@test"
        )
        menu = Menu.objects.create(show_text="Test", date="2022-01-01")
        self.order = Order.objects.create(menu=menu, staff=self.staff)

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

    def test_order_retrieve(self):
        request = self.factory.get(f"/order/{self.order.uuid}")
        response = OrderRetrieveViewAPI.as_view()(request, uuid=self.order.uuid)
        self.assertEqual(response.status_code, 200)

    def test_staff_retrieve(self):
        request = self.factory.get(f"/{self.staff.id}")
        request.user = self.user
        response = StaffViewRetrieveAPI.as_view()(request, pk=self.staff.id)
        self.assertEqual(response.status_code, 200)

    def test_staff_list(self):
        request = self.factory.get("")
        request.user = self.user
        response = StaffViewAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)
