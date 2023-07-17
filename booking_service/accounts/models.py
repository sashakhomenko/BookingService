from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


def get_file_path(instance, filename):
    return f'user_{instance.id}/{filename}'


class CustomUser(AbstractUser):
    email = models.EmailField(_('Email address'), unique=True, blank=True, null=True)
    phone = models.CharField(_('Phone number'), unique=True, blank=True, null=True)
    avatar = models.ImageField(_('Avatar'), upload_to=get_file_path, blank=True, null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
