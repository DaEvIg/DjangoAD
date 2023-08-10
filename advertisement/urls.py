from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from ad.views import AdViewSet

router = routers.SimpleRouter()
router.register(r'advertisement', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),          # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
]