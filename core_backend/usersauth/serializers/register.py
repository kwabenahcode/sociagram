from user.models import *
from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            # 'bio',
            # 'avatar',
            'first_name',
            'last_name',
            'password'
        ]
        extra_fields = {'password': {'write_only':'True'} }