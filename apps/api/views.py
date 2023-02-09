from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from apps.api.serializers import ProductSerializer, ShopCategorySerializer
from apps.shop.models import Product,ShopCategory


class ProductListAPIView(ListAPIView): 
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_available=True)
    permission_classes = [IsAuthenticated]


class ShopCategoryListAPIView(ListAPIView):
    serializer_class = ShopCategorySerializer
    queryset = ShopCategory.objects.all()


