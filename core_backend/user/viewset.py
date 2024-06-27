from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ('patch', 'get')
    permission_classes = (AllowAny)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.is_superuser:
            user = User.objects.all()
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = User.objects.get_User_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        
        return obj
