from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        return True
        # if request.method in SAFE_METHODS:
        #     return True
        #
        # if request.method == ['POST']:
        #     return request.user.is_superuser
        #
        # return False

    def has_object_permission(self, request, view, obj):
        return True
