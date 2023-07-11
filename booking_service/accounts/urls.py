from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginAPIView, RegistrationAPIView, LogoutAPIView, UserAPIView


urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="create-user"),
    path("login/", LoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", LogoutAPIView.as_view(), name="logout-user"),
    path("profile/", UserAPIView.as_view(), name="user-info"),

    path('social/', include('rest_framework_social_oauth2.urls')),
]
