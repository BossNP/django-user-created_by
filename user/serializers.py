from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), 
        read_only=True
        )
    updated_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), 
        read_only=True
        )
    
    class Meta(object):
        model = User
        fields = '__all__'
