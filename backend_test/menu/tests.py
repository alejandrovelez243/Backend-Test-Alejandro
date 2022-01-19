from datetime import datetime

from django.test import TestCase, override_settings
from rest_framework.test import APIRequestFactory

from backend_test.staff.models import Order, Staff, User

from .models import Menu, Product
from .serializers import MenuSerializer, MenuUpdateSerializer, ProductSerializer
from .tasks import send_slack_message
from .views import (
    MenuViewAPI,
    MenuViewRetrieveAPI,
    ProductViewAPI,
    ProductViewRetrieveAPI,
)

# Create your tests here.


class ModelsTest(TestCase):
    def test_objects_created(self):
        menu = Menu.objects.create(show_text="TEST", date=datetime.now().date())
        product = Product.objects.create(menu=menu, description="TEST product")
        self.assertEqual(menu.show_text, "TEST")
        self.assertEqual(product.menu, menu)
        self.assertEqual(str(menu), "TEST")
        self.assertEqual(str(product), "TEST product")


class SerializersTest(TestCase):
    def test_menu_serializer(self):
        menu = Menu.objects.create(show_text="TEST", date=datetime.now().date())
        serializer = MenuSerializer(menu)
        self.assertEqual(serializer.data.get("show_text"), "TEST")

    def test_product_serializer(self):
        menu = Menu.objects.create(show_text="TEST", date=datetime.now().date())
        product = Product.objects.create(menu=menu, description="TEST product")
        serializer = ProductSerializer(product)
        self.assertEqual(serializer.data.get("description"), "TEST product")
        self.assertEqual(serializer.data.get("menu"), menu.show_text)

    def test_menu_serializer_valid(self):
        menu = {
            "date": datetime.now().date(),
            "show_text": "TEST",
            "products": [
                {"description": "Test product 1"},
                {"description": "Test product 2"},
                {"description": "Test product 3"},
            ],
        }
        serializer = MenuSerializer(data=menu, many=False)
        self.assertTrue(serializer.is_valid())

    def test_menu_serializer_no_valid(self):
        menu = {
            "date": "FAIL",
            "show_text": "TEST",
            "products": [
                {"description": "Test product 1"},
                {"description": "Test product 2"},
                {"description": "Test product 3"},
            ],
        }
        serializer = MenuSerializer(data=menu, many=False)
        self.assertFalse(serializer.is_valid())

    def test_product_serializer_valid(self):
        product = {
            "description": "Test",
        }
        serializer = ProductSerializer(data=product, many=False)
        self.assertTrue(serializer.is_valid())

    def test_product_serializer_no_valid(self):
        product = {
            "descriptions": "Test",
        }
        serializer = ProductSerializer(data=product, many=False)
        self.assertFalse(serializer.is_valid())

    def test_menu_update_serializer_valid(self):
        menu = {"date": datetime.now().date(), "show_text": "TEST"}
        serializer = MenuUpdateSerializer(data=menu, many=False)
        self.assertTrue(serializer.is_valid())

    def test_menu_update_serializer_no_valid(self):
        menu = {"date": "FAIL", "show_text": "TEST"}
        serializer = MenuUpdateSerializer(data=menu, many=False)
        self.assertFalse(serializer.is_valid())


class ApiTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username="admin", password="abc1234*")

    def test_menu_creation(self):
        new_menu = {
            "date": "2022-01-01",
            "show_text": "TEST",
            "products": [{"description": "unique_product"}],
        }
        request = self.factory.post("/menu/", data=new_menu, format="json")
        request.user = self.user
        response = MenuViewAPI.as_view()(request)
        product = Product.objects.filter(description="unique_product").first()
        self.assertIsNotNone(product)
        self.assertEqual(response.status_code, 201)

    def test_menu_list(self):
        request = self.factory.get("/menu/")
        request.user = self.user
        response = MenuViewAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_menu_retrieve(self):
        menu = Menu.objects.create(show_text="TEST", date=datetime.now().date())
        request = self.factory.get(f"/menu/{menu.id}")
        request.user = self.user
        response = MenuViewRetrieveAPI.as_view()(request, pk=menu.id)
        self.assertEqual(response.data.get("show_text"), menu.show_text)
        self.assertEqual(response.status_code, 200)

    def test_product_list(self):
        request = self.factory.get("/menu/product")
        request.user = self.user
        response = ProductViewAPI.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_product_retrieve(self):
        menu = Menu.objects.create(show_text="TEST", date=datetime.now().date())
        product = Product.objects.create(menu=menu, description="Test")
        request = self.factory.get(f"menu/products/{product.id}")
        request.user = self.user
        response = ProductViewRetrieveAPI.as_view()(request, pk=product.id)
        self.assertEqual(response.data.get("description"), product.description)
        self.assertEqual(response.status_code, 200)


class TasksTest(TestCase):
    def setUp(self):
        menu = Menu.objects.create(show_text="TEST", date=datetime.now().date())
        staff = Staff.objects.create(
            full_name="Alejandro", email="alejandro-243@hotmail.com", slack_user="@alejandro-243"
        )
        Order.objects.create(menu=menu, staff=staff)

    @override_settings(CELERY_ALWAYS_EAGER=True)
    def test_send_slack_message(self):
        message = send_slack_message.delay()
        print(message.get())
        self.assertEqual(message.get(), True)
