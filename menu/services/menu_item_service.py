from menu.serializers.menu_item_serializers import MenuItemSaveSerializer
from rest_framework.exceptions import ValidationError

class MenuItemService:
    
    def save(self, request):
        serializer = MenuItemSaveSerializer(data=request.data, context={"restaurant": request.user.restaurant})
        if serializer.is_valid():
            menu_item_saved = serializer.save()
            menu_item_saved = MenuItemSaveSerializer(menu_item_saved)
            return menu_item_saved.data
        
        raise ValidationError(serializer.errors)