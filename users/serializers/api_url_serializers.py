from rest_framework import serializers
from users.models.api_url import ApiUrl

class ApiUrlSaveSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = ApiUrl
        fields = ['id', 'name', 'url', 'method']
        
        