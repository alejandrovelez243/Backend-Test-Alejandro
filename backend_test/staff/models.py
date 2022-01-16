from django.db import models
from django.contrib.auth.models import AbstractUser
from backend_test.menu.models import Menu
import uuid

# Create your models here.

class User(AbstractUser):
    """
    Abstract user from django, to have manage of the models migration.
    """
    pass

class Staff(models.Model):
    """
    """
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    slack_user = models.CharField(max_length=50)


class Order(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)
    customizations = models.TextField(blank=True, null=True)
