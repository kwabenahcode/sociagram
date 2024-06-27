from user.models import *
from serializers.register import RegisterUserSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated


class RegisterUserViewSet(viewsets.ViewSet):
    """
        User creation viewset
    """
    http_method_names = ('post')
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            username = serializer.data['username']
            password = serializer.data['password']

            if len(password) < 4:
                return Response{
                    'status':'failure',
                    'detail': 'Password must be more than four'
                    s

                }




