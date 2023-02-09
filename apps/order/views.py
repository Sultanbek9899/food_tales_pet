from django.shortcuts import render


# Create your views here.
from django.views.generic import FormView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from apps.order.models import Order, OrderItem
from apps.order.forms import OrderForm

from apps.cart.cart import Cart

class CreateOrderView(LoginRequiredMixin,FormView):
    form_class = OrderForm
    model = Order
    success_url = reverse_lazy("success_created")


    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user
        order.status = Order.STATUS_NEW
        order.save()
        
        cart = Cart(self.request)
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"]
            )
        cart.clear()
        return super().form_valid(form)



class OrderCreatedView(TemplateView):
    template_name = "order_created.html"



class UserOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "my_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user)
        return qs