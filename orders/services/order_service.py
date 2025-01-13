from orders.serializers.order_serializers import OrderSaveSerializer, OrderInvalidSerializer, OrderSerializer
from rest_framework.exceptions import ValidationError
from menu.models.menu_item import MenuItem
from django.db import transaction
from orders.models.order_item import OrderItem

class OrderService:
    def save(self, data, user_auth):
        serializer = OrderSaveSerializer(data=data)
        if serializer.is_valid():
            order_items = serializer.validated_data['order_items']
            invalid_items = []
            total_amount = 0

            for order_item in order_items:
                menu_item = MenuItem.objects.filter(id=order_item['id'], active=True).first()
                if not menu_item:
                    invalid_items.append(order_item['id'])
                else:
                    item_total = menu_item.price * order_item['quantity']
                    total_amount += item_total

            if len(invalid_items) > 0:
                data_object = {
                    "reason": "Some items are invalid or inactive.",
                    "invalid_items": invalid_items
                }
                serializer_invalid_items = OrderInvalidSerializer(data_object)
                return False, serializer_invalid_items.data

            try:
                order_data = serializer.validated_data
                order_data['total_amount'] = total_amount
                order_data['customer_id'] = user_auth.id

                with transaction.atomic():
                    order_saved = serializer.save() 

                    order_serializer = OrderSerializer(order_saved)
                    order_items_details = OrderItem.objects.filter(order=order_saved)
                    menu_items = []
                    for order_item in order_items_details:
                        menu_item_data = {
                            'id': order_item.menu_item.id,
                            'name': order_item.menu_item.name,
                            'price': str(order_item.menu_item.price),
                            'quantity': order_item.quantity
                        }
                        menu_items.append(menu_item_data)

                    return True, {
                        "order": order_serializer.data,
                        "order_items": menu_items
                    }

            except Exception as e:
                print(e)

        raise ValidationError(serializer.errors)