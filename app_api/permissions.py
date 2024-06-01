from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        pass
        # Agar ko'rmoqchi bo'lgan profilimiz o'zimizniki bo'lsa,
        # unda ko'ra olishimiz, o'zgartira olishimiz va o'chira olishimiz

        # Istisno tariqasida superuser bo'lishi mumkin
