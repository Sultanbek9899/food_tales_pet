from django.db import models

# Create your models here.
from apps.accounts.models import User
from apps.shop.models import Product


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_CONFIRMED= "confirmed"
    STATUS_REJECTED="rejected"
    STATUS_DELIVERED="delivered"
    STATUS_ARCHIVED="archived"
    
    STATUS_CHOICES = (
        (STATUS_NEW, "Новый"),
        (STATUS_CONFIRMED, "Подтвержден"),
        (STATUS_REJECTED, "Отменен"),
        (STATUS_DELIVERED, "Доставлен"), 
        (STATUS_ARCHIVED, "Архивирован"),
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    address = models.CharField("Адрес", max_length=255)
    mobile = models.CharField("Номер телефона", max_length=15)
    status = models.CharField("Статус", max_length=10, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Заказ"
        verbose_name_plural="Заказы"
        ordering = ["-created"]
    

    def __str__(self):
        return f"Заказ #{self.id}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField("Количество")

    class Meta:
        verbose_name="Товар заказа"
        verbose_name_plural="Товары заказа"
        ordering = ["-quantity"]





