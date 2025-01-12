from rest_framework.views import APIView
from restaurantsystem.utils.api_response import ApiSuccessResponse, ApiErrorResponse
from rest_framework.permissions import AllowAny, IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status 
from users.services.api_url_service import ApiUrlService

class ApiUrlSaveController(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def __init__(self, api_url_service=None):
        super().__init__()
        self.api_url_service = api_url_service or ApiUrlService()
    
    def post(self, request):
        if request.method == "POST":
            api_url_created = self.api_url_service.save(request.data)
            api_response = ApiSuccessResponse(201, api_url_created, "Api url created successfully")
            return Response(api_response.get_response(), status=status.HTTP_201_CREATED)     