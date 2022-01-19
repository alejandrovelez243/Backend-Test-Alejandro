from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Order, Staff

# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "slack_user")


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "staff", "menu")


admin.site.register(Staff, StaffAdmin)
admin.site.register(Order, OrderAdmin)
