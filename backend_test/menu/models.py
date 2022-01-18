from django.db import models
# Create your models here.


class Menu(models.Model):
    date = models.DateField(unique=True)
    show_text = models.TextField()

    def __str__(self):
        return self.show_text
    

class Product(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description
