from rest_framework.exceptions import ValidationError

from users.models.api_url import ApiUrl
from users.serializers.api_url_serializers import ApiUrlSaveSerializer

class ApiUrlService:
    
    def save(self, data):
        serializer = ApiUrlSaveSerializer(data=data)
        if serializer.is_valid():
            api_url_saved = serializer.save()
            api_url_serialized = ApiUrlSaveSerializer(api_url_saved)
            return api_url_serialized.data
        
        raise ValidationError(serializer.errors)
        