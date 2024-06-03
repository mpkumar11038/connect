from django.urls import path
from .views import SignupView, UserSearchView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('search/', UserSearchView.as_view(), name='user-search'),
]
