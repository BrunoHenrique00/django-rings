from django.urls import path, include
from .views import AnelViewSet, index

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rings', AnelViewSet, basename='rings')

urlpatterns = [
    path('', include(router.urls)),
]