from apps.shop.models import Product, ShopCategory
from rest_framework import serializers


class ShopCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  ShopCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



