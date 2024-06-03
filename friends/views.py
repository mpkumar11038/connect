from datetime import timedelta

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import FriendRequest
from .serializers import FriendRequestSerializer

User = get_user_model()


class FriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        to_user_id = self.request.data.get('to_user')
        to_user = User.objects.get(id=to_user_id)
        from_user = self.request.user

        if from_user == to_user:
            raise ValidationError("You cannot send a friends request to yourself.")

        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user).exists():
            raise ValidationError("Friend request already sent.")

        recent_requests = FriendRequest.objects.filter(from_user=from_user,
                                                       created_at__gte=timezone.now() - timedelta(minutes=1))
        if recent_requests.count() >= 3:
            raise ValidationError("You cannot send more than 3 friends requests within a minute.")

        serializer.save(from_user=from_user, to_user=to_user)


class RespondFriendRequestView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        request_id = self.kwargs['pk']
        friend_request = FriendRequest.objects.get(id=request_id)
        if friend_request.to_user != self.request.user:
            raise ValidationError("You are not allowed to respond to this friends request.")
        return friend_request

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()
        status = request.data.get('status')

        if status not in ['accepted', 'rejected']:
            raise ValidationError("Invalid status. Valid statuses are 'accepted' or 'rejected'.")

        friend_request.status = status
        friend_request.save()
        return Response(FriendRequestSerializer(friend_request).data)
