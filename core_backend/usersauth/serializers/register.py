from user.models import User
from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 
            'email',
            'username',
            # 'bio',
            # 'avatar',
            'first_name',
            'last_name',
            'password'
        ]
        extra_fields = {'password': {'write_only':'True'} }