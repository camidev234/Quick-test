from rest_framework import serializers

class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True, min_value=1)
    
    class Meta:
        fields = ['id', 'quantity']