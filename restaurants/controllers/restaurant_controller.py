from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from restaurantsystem.utils.api_response import ApiSuccessResponse, ApiErrorResponse
from restaurants.services.restaurant_service import RestaurantService



class RestaurantSaveController(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def  __init__(self, restaurant_service=None):
        super().__init__()
        self.restaurant_service = restaurant_service or RestaurantService()
    
    def post(self, request):
        if request.method == "POST":
            restaurant_created = self.restaurant_service.save(request.data)
            api_response = ApiSuccessResponse(201, restaurant_created, "Restaurant created sucessfully")
            return Response(api_response.get_response(), status=status.HTTP_201_CREATED)
        
        