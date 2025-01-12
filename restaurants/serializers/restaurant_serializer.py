from rest_framework import serializers
from restaurants.models.restaurant import Restaurant

class RestaurantSaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'category', 'latitude', 'longitude']