from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginAPIView, RegistrationAPIView, LogoutAPIView, UserAPIView, VerifyEmailAPIView, \
    RequestPasswordResetEmailAPIView, PasswordTokenCheckAPIView, SetNewPasswordAPIView

urlpatterns = [
    path("register/", RegistrationAPIView.as_view(), name="create-user"),
    path("email-verify/", VerifyEmailAPIView.as_view(), name="email-verify"),
    path("login/", LoginAPIView.as_view(), name="login-user"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", LogoutAPIView.as_view(), name="logout-user"),
    path("profile/", UserAPIView.as_view(), name="user-info"),

    path("request-password-reset-email/", RequestPasswordResetEmailAPIView.as_view(),
         name="request-password-reset-email"),
    path("password-reset/<uidb64>/<token>/", PasswordTokenCheckAPIView.as_view(), name="password-reset-confirm"),
    path("password-reset-complete/", SetNewPasswordAPIView.as_view(), name='password-reset-complete'),

    path('social/', include('rest_framework_social_oauth2.urls')),
]
