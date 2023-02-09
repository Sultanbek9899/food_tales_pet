from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from django.views import View
from django.contrib import messages

from .cart import Cart
from apps.shop.models import Product
from apps.order.forms import OrderForm

class CartPageView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["order_form"] = OrderForm()
        return context

class AddCartView(View):

    def get(self,request,product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.add(
            product=product,
            quantity=1
        )
        messages.add_message(request,messages.SUCCESS, "Ваш товар добавлен в корзину!")
        return redirect("product_list")



class DeleteProductCartView(View):

    def get(self,request, product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.remove(product)
        return redirect("cart_page")


class ClearCartView(View):

    def get(self,request):
        cart = Cart(request)
        cart.clear()
        return redirect("cart_page")