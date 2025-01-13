from rest_framework.exceptions import ValidationError
from restaurants.serializers.menu_category_serializers import MenuCategorySaveSerializer

class MenuCategoryService:
    
    def save(self, data, user_auth):
        restaurant = user_auth.restaurant
        serializer = MenuCategorySaveSerializer(data=data, context={"restaurant": restaurant})
        
        if serializer.is_valid():
            menu_category_saved = serializer.save()
            menu_category_saved = MenuCategorySaveSerializer(menu_category_saved)
            return menu_category_saved.data
            
        raise ValidationError(serializer.errors)