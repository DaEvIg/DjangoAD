from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated or request.user.is_staff
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['retrieve', 'list']:
            return True
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return obj.id == request.user.id or request.user.is_staff
        else:
            return False

class IsAdminOrIsSelf(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method not in permissions.SAFE_METHODS:
            return obj.id == request.user.id or request.user.is_staff

