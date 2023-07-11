from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'phone',)


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        phone = attrs.get('phone')
        password = attrs.get('password')

        try:
            if email:
                user = CustomUser.objects.get(email=email)
            elif phone:
                user = CustomUser.objects.get(phone=phone)
            else:
                raise serializers.ValidationError(_('Invalid credentials'))
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError(_('Invalid credentials'))

        if not user.check_password(password) or not user.is_active:
            raise serializers.ValidationError(_('Invalid credentials'))

        return user
