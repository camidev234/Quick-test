from restaurants.serializers.restaurant_serializer import RestaurantSaveSerializer
from rest_framework.exceptions import ValidationError

class RestaurantService:
    
    def save(self, data):
        serializer = RestaurantSaveSerializer(data=data)
        if serializer.is_valid():
                restaurant_created = serializer.save()
                restaurant_serialized = RestaurantSaveSerializer(restaurant_created)
                return restaurant_serialized.data
            
        raise ValidationError(serializer.errors)