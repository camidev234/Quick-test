from menu.serializers.menu_item_serializers import MenuItemSaveSerializer, MenuItemGetSerializer
from rest_framework.exceptions import ValidationError, NotFound
from menu.models.menu_item import MenuItem

class MenuItemService:
    
    def save(self, request):
        serializer = MenuItemSaveSerializer(data=request.data, context={"restaurant": request.user.restaurant})
        if serializer.is_valid():
            menu_item_saved = serializer.save()
            menu_item_saved = MenuItemSaveSerializer(menu_item_saved)
            return menu_item_saved.data
        
        raise ValidationError(serializer.errors)
    
    def get_item_instance(self, pk):
        try:
            item = MenuItem.objects.get(id=pk)
            return item
        except MenuItem.DoesNotExist:
            raise NotFound("The item does not exists")
        
    def get_item_by_id(self, pk):
        item = self.get_item_instance(pk)
        serializer = MenuItemGetSerializer(item)
        return serializer.data
        