from rest_framework.views import APIView
from restaurants.services.restaurant_service import RestaurantService

class RestaurantSaveController(APIView):
    
    def  __init__(self, restaurant_service=None):
        super().__init__()
        self.restaurant_service = restaurant_service or RestaurantService()
    
    def post(self, request):
        pass