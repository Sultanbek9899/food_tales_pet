from django.contrib import admin

# Register your models here.
from apps.order.models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ["address", "mobile", "user", "status", "id"]
    list_filter = ["status", "created"]
    list_editable = ["status"]

