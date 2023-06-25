from rest_framework.permissions import BasePermission


class IsOwnerProfileOrIsAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.user == request.user