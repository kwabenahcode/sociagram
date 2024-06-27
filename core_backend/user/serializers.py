from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.CharField(read_only=True)
    updated = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 
                  'username', 
                  'email', 
                  'first_name', 
                  'last_name', 
                  'bio',
                  'avatar',
                  'created',
                  'updated',
                  'is_active',
                  ]
        read_only_field = ['is_active']
        
    
