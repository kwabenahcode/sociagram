from user.models import *
from rest_framework import serializers

class RegisterUserRerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            'eamil',
            'username',
            'bio',
            'first_name',
            'last_name',
            'avatar'
        ]
        extra_fields = {'password': {'write_only':'True'} }