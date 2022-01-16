from django.db import models
from django.contrib.auth.models import AbstractUser
from backend_test.menu.models import Menu

# Create your models here.

class User(AbstractUser):
    """
    Abstract user from django, to have manage of the models migration.
    """
    pass

class Staff(models.Model):
    """
    """
    
    email = models.EmailField()
    slack_user = models.CharField(max_length=50)


class Order(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    customizations = models.TextField()
