from rest_framework import serializers

from .models import FriendRequest


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'created_at', 'status']
        read_only_fields = ['from_user', 'created_at', 'status']
