from rest_framework import serializers

from .models import Customer, Gender

class CustomerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), 
        read_only=True
        )
    updated_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), 
        read_only=True
        )
    
    class Meta:
        model = Customer
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), 
        read_only=True
        )
    updated_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), 
        read_only=True
        )
    
    class Meta:
        model = Gender
        fields = '__all__'