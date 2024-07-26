from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Разрешить только чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить остальные действия только администраторам
        return request.user and request.user.is_staff
