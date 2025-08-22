from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache
from .serializers import LocationAutoCompleteSerializer
from rest_framework import permissions
from .models import BloodRequest,BloodRequestComment
from .serializers import BloodRequestSerializer, BloodRequestCommentSerializer
from rest_framework.decorater import action
from rest_framework.response import Response
from authentication.models import Location


class BloodRequestViewSet(ModelViewSet):
    queryset = BloodRequest.objects.all().order_by('-created_at')
    serializer_class = BloodRequestSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(
        detail=True,
        method=['GET','POST'],
        serializer_class=BloodRequestCommentSerializer,
        permission_classes=[permissions.IsAuthenticated]
    )
    def comment(self, request, pk, *args, **kwargs):
        blood_request = self.get_object()
        if request.method == 'POST':
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            BloodRequestComment.objects.create(
                user=request.user,
                text=serializer.validated_data.get("text"),
                request=blood_request
            )
            return Response("Posted Successfully")
        comments = BloodRequestComment.objects.filter(request=blood_request)
        serializer = self.get_serializer(comments, many=True)
        return Response(serializer.data)
    



class LocationAutoCompleteViewSet(ModelViewSet):
    queryset = (
        Location.objects.all()
        .select_related("district", "district__province")
    )
    serializer_class = LocationAutoCompleteSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        cache_key = f"static_key_locations_autocomplete"
        data = cache.get(cache_key)
        if data:
            return Response(data)

        data = serializer.data
        cache.set(cache_key, data, timeout=None)
        return Response(data)





    
