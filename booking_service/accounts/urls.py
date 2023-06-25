from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileDetailView, UserProfileListCreateView


urlpatterns = [
    path('profiles/', UserProfileListCreateView.as_view(), name='profiles'),
    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile'),
]