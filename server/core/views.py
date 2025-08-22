from rest_framework import viewsets, permissions
from .models import BloodRequest,BloodRequestComment
from .serializers import BloodRequestSerializer, BloodRequestCommentSerializer
from rest_framework.decorater import action
from rest_framework.response import Response


class BloodRequestViewSet(viewsets.ModelViewSet):
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



    
