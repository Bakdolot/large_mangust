from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "item"]
    search_fields = ["customer", "item"]
