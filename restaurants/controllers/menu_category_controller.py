from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from restaurantsystem.utils.api_response import ApiSuccessResponse, ApiErrorResponse
from restaurants.services.menu_category_service import MenuCategoryService

class MenuCategorySaveController(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, menu_category_service=None):
        super().__init__()
        self.menu_category_service = menu_category_service or MenuCategoryService()
    
    def post(self, request):
        if request.method == "POST":
            menu_category_created = self.menu_category_service.save(request.data, request.user)
            api_response = ApiSuccessResponse(201, menu_category_created, "Menu category created successfully")
            return Response(api_response.get_response(), status=status.HTTP_201_CREATED)