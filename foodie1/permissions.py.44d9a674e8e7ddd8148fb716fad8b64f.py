from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            if request.user and request.user.groups.filter(name='vendors'):
                return True
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return obj.vendor.id == request.user.id


class IsVendor(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='vendors'):
            return True
        return False


class IsVendorAndOwner(IsVendor):
    def has_object_permission(self, request, view, obj):
        return obj.vendor.id == request.user.id or request.user.is_superuser


class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsAccountOwner(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return request.user.is_active
        elif view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_superuser
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True
