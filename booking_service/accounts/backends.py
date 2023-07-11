from .models import CustomUser
from django.db.models import Q


class AuthBackend(object):
    def authenticate(self, request, email, phone, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(Q(email=email) | Q(phone=phone))
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None