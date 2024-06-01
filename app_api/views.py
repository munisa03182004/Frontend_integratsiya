from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from . import serializers
from . import permissions

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrSuperuser]

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_superuser or request.user.id != kwargs.get('pk'):
            return Response(data={"detail": "You don't have permission to perform this action"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.user.is_superuser or request.user.id != kwargs.get('pk'):
            return Response(data={"detail": "You don't have permission to perform this action"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        if not request.user.is_superuser or request.user.id != kwargs.get('pk'):
            return Response(data={"detail": "You don't have permission to perform this action"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response(data={"detail": "You don't have permission to perform this action"},
                            status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
