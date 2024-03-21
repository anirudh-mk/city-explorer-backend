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


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
        ]

    def update(self, instance, validated_data):
        instance.priority_locations = validated_data.get('priority_locations', instance.priority_locations)
        instance.save()
        return instance
