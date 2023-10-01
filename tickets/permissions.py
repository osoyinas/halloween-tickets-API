from rest_framework import permissions

class IsStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario autenticado es un miembro del staff
        return request.user.is_authenticated and request.user.is_staff