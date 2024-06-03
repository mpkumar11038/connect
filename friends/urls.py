from django.urls import path
from .views import FriendRequestView, RespondFriendRequestView

urlpatterns = [
    path('send-friends-request/', FriendRequestView.as_view(), name='send-friends-request'),
    path('respond-friends-request/<int:pk>/', RespondFriendRequestView.as_view(), name='respond-friends-request'),
]
