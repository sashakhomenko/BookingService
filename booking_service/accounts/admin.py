from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone', 'avatar']


admin.site.register(CustomUser, CustomUserAdmin)
