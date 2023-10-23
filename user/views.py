from .serializers import RegisterSerializer,CustomTokenObtainPairSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
  
    user = authenticate(request, username=username, password=password)
   
    if user is not None:
        custom_token_serializer = CustomTokenObtainPairSerializer()
        token = custom_token_serializer.get_token(user)
        access_token = str(token)
        
        return Response({'token': access_token}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Not found user"}, status=status.HTTP_400_BAD_REQUEST)

