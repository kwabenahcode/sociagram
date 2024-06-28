from user.models import *
from usersauth.serializers.register import RegisterUserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

import re

class RegisterUserViewSet(viewsets.ViewSet):
    """
        User creation viewset
    """
    http_method_names = ['post']
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            if len(password) < 4:
                return Response(
                    {
                        "status":"failure", 
                        "detail":"Password must be at least 4"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            if email is None or password is None:
                return Response(
                    {
                        "status": "failure",
                        "detail": "Provide both email and password"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if User.objects.filter(email=email).exists():
                return Response(
                    {
                        'status':'failure',
                        'detail': 'Email already exist',
                    },
                    status=status.HTTP_208_ALREADY_REPORTED
                )
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return Response(
                    {
                        'status':"failure",
                        'detail': "The email format is not valid"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            user = self.create_user(email=email, username=username, password=password)
            user.save()
            refresh = RefreshToken.for_user(user)
            res = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response(
                {
                    'status': "success",
                    'user': serializer.data,
                    'refresh':res['refresh'],
                    'token':res['access'],
                    "detail": 'Successfully created your account'
                    
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "status": "failure",
                'detail': serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def create_user(self, email, username, password):
        user = User(
            email=email,
            username = username,
        )
        user.set_password(password)

        return user








                    

                




