import imp
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_superuser
        )


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_staff
        )
