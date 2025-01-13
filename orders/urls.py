from django.urls import path
from orders.controllers.order_controller import OrderSaveController

urlpatterns = [
    path('orders/', OrderSaveController.as_view(), name="save_order")
]