from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsTutorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'tutor' or request.user.is_staff:
            return True
