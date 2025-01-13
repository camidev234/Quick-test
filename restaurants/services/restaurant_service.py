from restaurants.serializers.restaurant_serializer import RestaurantSaveSerializer
from rest_framework.exceptions import ValidationError
from restaurants.models.restaurant import Restaurant

class RestaurantService:
    
    def save(self, data):
        serializer = RestaurantSaveSerializer(data=data)
        if serializer.is_valid():
                restaurant_created = serializer.save()
                restaurant_serialized = RestaurantSaveSerializer(restaurant_created)
                return restaurant_serialized.data
            
        raise ValidationError(serializer.errors)
    
    def get_all_restaurants(self):
        restaurants = Restaurant.objects.all().order_by('id')
        return restaurants