from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """Foydalanuvchi ma'lumotlarini serializer"""
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'date_joined']

class RegisterSerializer(serializers.ModelSerializer):
    """Ro‘yxatdan o‘tish uchun serializer"""
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    """Telefon raqam orqali tizimga kirish"""
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(phone_number=data['phone_number'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Telefon raqam yoki parol noto‘g‘ri")
        return user