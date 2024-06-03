from django.urls import path
from .views import FriendRequestView, RespondFriendRequestView, ListFriendsView, ListPendingFriendRequestsView

urlpatterns = [
    path('send-friend-request/', FriendRequestView.as_view(), name='send-friend-request'),
    path('respond-friend-request/<int:pk>/', RespondFriendRequestView.as_view(), name='respond-friend-request'),
    path('list-friends/', ListFriendsView.as_view(), name='list-friends'),
    path('pending-friend-requests/', ListPendingFriendRequestsView.as_view(), name='pending-friend-requests'),
]
