from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
        Querry the user model to get and return all the users excluding the superusers 
        and also get the users by their public id.
    """

    http_method_names = ('patch', 'get')
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = User.objects.get_User_object_by_public_id(self.kwargs['pk'])
        #check if the user has the permission to perform this request
        self.check_object_permissions(self.request, obj)
        #returns the user object
        return obj
