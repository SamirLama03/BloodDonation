from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BloodRequestViewSet

router = DefaultRouter()
router.register(r'emergency-requests', BloodRequestViewSet, basename='emergency-request')

urlpatterns = [
    path('', include(router.urls)),
]
