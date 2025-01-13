from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from restaurantsystem.utils.api_response import ApiSuccessResponse, ApiErrorResponse
from restaurantsystem.utils.paginator import Paginator
from menu.services.menu_item_service import MenuItemService

class MenuItemSaveController(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, menu_item_service=None):
        super().__init__()
        self.menu_item_service = menu_item_service or MenuItemService()
        
    def post(self, request):
        menu_item_saved = self.menu_item_service.save(request)
        api_repsonse = ApiSuccessResponse(201, menu_item_saved, "Menu item created successfully")
        return Response(api_repsonse.get_response(), status=status.HTTP_201_CREATED)
    
class MenuItemGetController(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, menu_item_service=None):
        super().__init__()
        self.menu_item_service = menu_item_service or MenuItemService()
        
    def get(self, request, pk):
        item = self.menu_item_service.get_item_by_id(pk)
        api_response = ApiSuccessResponse(200, item, "Menu item found sucessfully")
        return Response(api_response.get_response(), status=status.HTTP_200_OK)