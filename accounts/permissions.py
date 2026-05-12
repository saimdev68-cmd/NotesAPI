from rest_framework.permissions import BasePermission

class NoCreateDeletePermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['create','destroy']:
            return False
        return request.user.is_authenticated
    
class IsStaffOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_staff
        )