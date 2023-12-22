from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *

class UserProfileSerializer(serializers.ModelSerializer):
    
    def update(self, instance, validated_data):
        # Retain the existing photo if 'photo' field is not present in the validated data
        if 'photo' not in validated_data:
            validated_data['photo'] = instance.photo
        return super().update(instance, validated_data)

    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username if obj.user else None
    
    def get_password(self, obj):
        return obj.user.password if obj.user else None
    
    class Meta:
        model = UserProfile
        fields = (
            "id",
            "username",
            "email",
            "phone_number",
            "photo"
        )
        
class ProductSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()  # Serialize UserProfile related to Product

    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailSerializer(ProductSerializer):
    owner = UserProfileSerializer()  # Serialize UserProfile related to Product

    # phone_number = serializers.SerializerMethodField()

    # def get_phone_number(self, obj):
    #     original_number = obj.owner.phone_number if hasattr(obj, 'owner') else None
    #     if original_number:
    #         # Check if the phone number starts with '0' and replace it with 'wa.me/62'
    #         if original_number.startswith('0'):
    #             return f"62{original_number[1:]}"
    #     return original_number

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'get_image',
            'get_thumbnail',
            'price',
            'get_image',
            'owner'
        )
