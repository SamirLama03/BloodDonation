from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    BloodRequestViewSet, 
    LocationAutoCompleteViewSet, 
    HospitalViewSet
)

router = DefaultRouter()
router.register('hospital', BloodRequestViewSet, basename='hospital')
router.register('location-autocomplete', LocationAutoCompleteViewSet, basename='location-autocomplete')
router.register('emergency-requests', HospitalViewSet, basename='emergency-request')

urlpatterns = [
    path('', include(router.urls)),
]
