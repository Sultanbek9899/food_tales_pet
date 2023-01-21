from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.shop.models import Product



class ProductListView(ListView):
    template_name="product_list.html"
    model = Product
    queryset = Product.objects.filter(is_available=True)


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product
    queryset = Product.objects.filter(is_available=True)


    