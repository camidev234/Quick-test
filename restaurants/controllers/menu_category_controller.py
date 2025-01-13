from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from restaurantsystem.utils.api_response import ApiSuccessResponse, ApiErrorResponse
from restaurantsystem.utils.paginator import Paginator
from restaurants.services.menu_category_service import MenuCategoryService
from restaurants.serializers.menu_category_serializers import MenuCategoryGetSerializer

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
        
class MenuCategoryListController(APIView):
    permission_classes = [IsAuthenticated]
    
    def __init__(self, menu_category_service=None, paginator=None):
        super().__init__()
        self.menu_category_service = menu_category_service or MenuCategoryService()
        self.paginator = paginator or Paginator()
        
    def get(self, request):
        try:
            self.paginator.validate_query_param(request)
            categories = self.menu_category_service.get_all_menu_categories(request)
            paginated_categories = self.paginator.paginate_query_set(categories, request)
            serialized_categories = MenuCategoryGetSerializer(paginated_categories, many=True)
            
            paginator_object = self.paginator.get_paginator_object()
            
            return paginator_object.get_paginated_response(serialized_categories.data)
        except Exception as e:
            print(e)  
            # error = {"error": "El parámetro 'page_size' debe ser un número válido"}   
            # api_response = ApiErrorResponse(400, message=error)
            # return Response(
            #     api_response.get_response(),
            #     status=status.HTTP_400_BAD_REQUEST
            # )