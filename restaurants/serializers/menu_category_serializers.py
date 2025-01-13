from rest_framework import serializers
from restaurants.models.menu_category import MenuCategory
from restaurants.models.restaurant import Restaurant

class MenuCategorySaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuCategory
        fields = ['id', 'category_name']
        
    def create(self, validated_data):
        restaurant = self.context.get('restaurant')
        if not restaurant:
            raise serializers.ValidationError("Restaurant context is required.")
   
        return MenuCategory.objects.create(restaurant=restaurant, **validated_data)