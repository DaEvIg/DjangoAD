import requests
from rest_framework.permissions import *
from .models import Ad, AdManager
from rest_framework import viewsets
from .permissions import UserPermission, IsAdminOrIsSelf
from .serializers import AdSerializer
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = (UserPermission,)
    decorator_permission = (IsAdminOrIsSelf,)
    @action(detail=False, permission_classes=decorator_permission)
    def all_deleted_ads(self, request, *args, **kwargs):
        deleted_ads = Ad.objects.deleted_only().filter(author=request.user)
        serializer = self.get_serializer(deleted_ads, many=True)
        return Response(serializer.data)
    @action(detail=True, permission_classes=decorator_permission)
    def deleted_ad(self, request, pk=None, *args, **kwargs):
        deleted_ad = Ad.deleted_objects.get(pk=pk, author=request.user.id)
        serializer = self.get_serializer(deleted_ad)
        return Response(serializer.data)
    @action(detail=False, permission_classes=decorator_permission)
    def undeleted_ads(self, request, *args, **kwargs):
        deleted_ads = Ad.objects.deleted_only()
        undeleted_ads = deleted_ads.undelete()
        serializer = self.get_serializer(Ad.objects.all().filter(author=request.user.id), many=True)
        return Response(serializer.data)