import uuid

from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'email',
            'password',
        ]

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data['username'] = self.initial_data.get('email')
        return User.objects.create_user(**validated_data)

