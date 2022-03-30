from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        elif view.action == 'create':
            if request.user and request.user.groups.filter(name='vendors'):
                return True

    def has_object_permission(self, request, view, obj):
        print(12345678900, request.user.username.objects.vendor.username, 12345678990)
        return obj.vendor == request.user


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
        if view.action == 'create':
            return request.user.is_anonymous or request.user.is_superuser
        elif view.action in ['update', 'partial_update', 'destroy', 'retrieve']:
            return request.user.is_active
        else:
            return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user.username == obj.username