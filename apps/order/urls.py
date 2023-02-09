from django.urls import path

from apps.order import views 

urlpatterns = [
    path("create/", views.CreateOrderView.as_view(), name="create_order"),
    path("success/created/", views.OrderCreatedView.as_view(), name="success_created"),
    path("my/orders/list/", views.UserOrdersView.as_view(), name="my_orders"),
]