from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CustomUser
        fields = ('username', 'email')
        extra_kwargs = {'password': {'write_only': True}}  #只能寫入

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        phone = validated_data['phone']

        if not username:
            raise ValueError('Username is required')
        
        if not email:
            raise ValueError('Email is required')
        
        if not phone:
            raise ValueError('Phone is required')

        user = CustomUser(username=username, email=email)
        user.set_password(validated_data['password'])
        user.save()         
       
        return user
    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom fields to the token payload
        token['sub'] = user.username
        token['admin'] = user.is_staff

        return token
            

