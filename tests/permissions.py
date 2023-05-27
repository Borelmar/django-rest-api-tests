from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from .models import Test
from users.models import User

class IsTutorOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'tutor' or request.user.is_staff:
            return True

class IsUserOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'user' or request.user.is_staff:
            return True

class IsTestOwner(BasePermission):
    def has_permission(self, request, view):
        test_id = view.kwargs.get('pk')
        try:
            if Test.objects.get(id=test_id, owner=request.user):
                if request.user.role == 'tutor' or request.user.is_staff:
                    return True
        except Test.DoesNotExist:
            return False
