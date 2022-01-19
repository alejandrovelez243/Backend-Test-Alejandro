import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from backend_test.menu.models import Menu, Product

# Create your models here.


class User(AbstractUser):
    """
    Abstract user from django, to have manage of the models migration.
    """

    pass


class Staff(models.Model):
    """ """

    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    slack_user = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=True, unique=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    customizations = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.staff}, {self.product}"
