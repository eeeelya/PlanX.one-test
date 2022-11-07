from rest_framework import permissions


class PermissionsForCategory(permissions.BasePermission):
    def has_permission(self, request, view):
        # only active users have permissions
        if not request.user.is_active:
            return False

        # superuser has all permissions
        if request.user.is_superuser:
            return True
        elif view.action == "create":  # non-superusers can only create
            return True

        return False
