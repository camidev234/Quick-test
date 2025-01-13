from rest_framework.exceptions import ValidationError
from restaurants.serializers.menu_category_serializers import MenuCategorySaveSerializer
from restaurants.models.menu_category import MenuCategory

class MenuCategoryService:
    
    def save(self, data, user_auth):
        restaurant = user_auth.restaurant
        serializer = MenuCategorySaveSerializer(data=data, context={"restaurant": restaurant})
        
        if serializer.is_valid():
            menu_category_saved = serializer.save()
            menu_category_saved = MenuCategorySaveSerializer(menu_category_saved)
            return menu_category_saved.data
            
        raise ValidationError(serializer.errors)
    
    def get_all_menu_categories(self, request):
        if request.user.restaurant:
            categories = MenuCategory.objects.filter(restaurant_id=request.user.restaurant.id).order_by('id')
            return categories
        else:
            categories = MenuCategory.objects.all().order_by('id')
            return categories
            