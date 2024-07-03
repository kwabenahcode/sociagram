from usersauth.serializers.login import LoginSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from user.models import *
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class LoginViewSet(viewsets.ViewSet):
    permission_classes  = (AllowAny,)
    serializer_class = LoginSerializer
    http_method_names = ['post']

    def login(self, request):
        serrializers = self.serializer_class(data=request.data)
        if serrializers.is_valid():
            email = serrializers.data['email']
            password = serrializers.data['password']

            if User.objects.filter(email=email):
                user = authenticate(email=email, password=password)
                if user is None:
                    return Response(
                        {
                            'status':'Failure',
                            'detail':'invalid credentials',
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
                refresh = RefreshToken.for_user(user)
                context = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token)

                }
                return Response (
                    {
                        'status': "success",
                        'detail': 'You have successfully Logged in',
                        'refresh':context['refresh'],
                        'access': context['access'],
                        'user': serrializers.data
                    },
                    status=status.HTTP_200_OK
                )