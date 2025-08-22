from rest_framework.viewsets import ModelViewSet
from django.core.cache import cache
from .serializers import LocationAutoCompleteSerializer
from rest_framework import permissions, status
from .models import BloodRequest,BloodRequestComment, Hospital, BloodDonationEvent
from .serializers import BloodRequestSerializer, BloodRequestCommentSerializer,HospitalSerializer, BloodDonationEventSerializer
from rest_framework.decorater import action
from rest_framework.response import Response
from authentication.models import Location
from rest_framework.serializer import Serializer


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
    

class HospitalViewSet(ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [permissions.IsAdminUser]


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




class BloodDonationEventViewSet(viewsets.ModelViewSet):
    queryset = BloodDonationEvent.objects.all().order_by('-start_datetime')
    serializer_class = BloodDonationEventSerializer
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=['post'], permissions=[permissions.IsAuthenticated], serializer_class=Serializer)
    def join(self, request, pk=None):
        """
        Join the event.
        """
        event = self.get_object()
        user = request.user
        if user in event.participants.all():
            return Response({"detail": "You have already joined this event."}, status=status.HTTP_400_BAD_REQUEST)
        event.participants.add(user)
        return Response({"detail": "Successfully joined the event."})

    @action(detail=True, methods=['post'],permissions=[permissions.IsAuthenticated], serializer_class=Serializer)
    def leave(self, request, pk=None):
        """
        Leave the event.
        """
        event = self.get_object()
        user = request.user
        if user not in event.participants.all():
            return Response({"detail": "You are not a participant of this event."}, status=status.HTTP_400_BAD_REQUEST)
        event.participants.remove(user)
        return Response({"detail": "Successfully left the event."}, status=status.HTTP_200_OK)

    
