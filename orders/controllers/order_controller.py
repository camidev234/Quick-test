from rest_framework.views import APIView
from restaurantsystem.utils.api_response import ApiSuccessResponse, ApiErrorResponse
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status 
from orders.services.order_service import OrderService
from restaurantsystem.utils.paginator import Paginator


class OrderSaveController(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, order_service=None):
        super().__init__()
        self.order_service = order_service or OrderService()
        
    def post(self, request):
        success, result = self.order_service.save(request.data, request.user)
        if success:
            api_response = ApiSuccessResponse(201, result, "Orden creada correctamente")
            return Response(api_response.get_response(), status=status.HTTP_201_CREATED)
        else:
            api_response = ApiErrorResponse(400, result, "An error ocurred")
            return Response(api_response.get_response(), status=status.HTTP_400_BAD_REQUEST)