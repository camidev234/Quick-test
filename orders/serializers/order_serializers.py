from rest_framework import serializers
from orders.serializers.order_item_serializers import OrderItemSerializer
from restaurants.models.restaurant import Restaurant
from orders.models.order import Order
from orders.models.order_item import OrderItem
from menu.models.menu_item import MenuItem

class OrderSaveSerializer(serializers.ModelSerializer):
    order_items = serializers.ListField(
        child=OrderItemSerializer(),
        required=True,
        allow_empty=False
    )
    
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(),
        source="restaurant",
        required=True
    )
    
    delivery_address = serializers.CharField(required=True)
    special_instructions = serializers.CharField(required=True)

    class Meta:
        model = Order
        fields = ['id', 'delivery_address', 'special_instructions', 'restaurant_id', 'order_items']

    def create(self, validated_data):
        
        order_items_data = validated_data.pop('order_items')

        order = Order.objects.create(**validated_data)
        
        # crea los Oorder item relacionados
        for order_item_data in order_items_data:
            menu_item = MenuItem.objects.get(id=order_item_data['id'])
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=order_item_data['quantity']
            )
        
        return order
        

class OrderInvalidSerializer(serializers.Serializer):
    
    reason = serializers.CharField()
    invalid_items = serializers.ListField(
        child=serializers.IntegerField(),
        required=True,
        allow_empty=False
    )
    
    class Meta:
        fields = ['reason', 'invalid_ids']
        
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'delivery_address', 'special_instructions', 'total_amount', 'restaurant']
