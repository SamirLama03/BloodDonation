from rest_framework import serializers
from .models import BloodRequest, Hospital, BloodRequestComment
from authentication.models import Location
from django.contrib.auth import get_user_model

User = get_user_model()


class BloodRequestCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = BloodRequestComment
        fields = [
            'user',
            'text',
            'created_at'
        ]


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'location']


class BloodRequestSerializer(serializers.ModelSerializer):

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request') 
        if request and request.method == "GET":
            fields['hospital'] = HospitalSerializer(read_only=True)
        else:
            fields['hospital'] = serializers.PrimaryKeyRelatedField(
                queryset=Hospital.objects.all()
            )
        return fields

    class Meta:
        model = BloodRequest
        fields = [
            'id',
            'requester',
            'hospital',
            'blood_type_needed',
            'units_needed',
            'urgency_level',
            'contact_person',
            'contact_number',
            'additional_notes',
            'is_fulfilled',
            'created_at', 'updated_at',
        ]
        read_only_fields = [
            'id', 
            'requester', 
            'created_at', 
            'updated_at'
        ]

    def create(self, validated_data):
        validated_data['requester'] = self.context['request'].user
        instance = super().create(validated_data)
        list_of_users_to_notify = (User.objects.filter(
            location=instance.location,
            blood_type=instance.blood_type_needed
        ).values_list("email",flat=True))
        # Yeta bata notify garine user list of users lai 
        return instance
    
class LocationAutoCompleteSerializer(serializer.ModelSerializer):
    district = serializers.ReadOnlyField(source="district.name")
    province = serializers.ReadOnlyField(source="district.province.name")

    class Meta:
        model = Location
        fields = [
            'id', 
            'name',
            'district',
            'province'
        ]
