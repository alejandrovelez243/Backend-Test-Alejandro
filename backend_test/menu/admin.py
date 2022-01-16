from django.contrib import admin
from .models import Menu, Product

# Register your models here.


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'show_text')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu', 'description')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Product, ProductAdmin)