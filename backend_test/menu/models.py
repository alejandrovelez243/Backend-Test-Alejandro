from django.db import models
# Create your models here.


class Menu(models.Model):
    date = models.DateField(unique=True)
    show_text = models.TextField()

class Product(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.TextField()

