from django.db import models
from django.conf import settings
from authentication.models import BLOOD_TYPE_CHOICES, Location


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='hospitals'
    )

    def __str__(self):
        return f"{self.name} - {self.location}"

LOW = 'Low'
MEDIUM ='Medium'
HIGH = 'High'
CRITICAL = 'Critical'
URGENCY_CHOICES = [
    (LOW, LOW),
    (MEDIUM, MEDIUM),
    (HIGH, HIGH),
    (CRITICAL, CRITICAL),
]

class BloodRequest(models.Model):
    requester = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blood_requests'
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='blood_requests'
    )
    blood_type_needed = models.CharField(
        max_length=3,
        choices=BLOOD_TYPE_CHOICES
    )
    units_needed = models.PositiveIntegerField(default=1) 
    urgency_level = models.CharField(  
        max_length=20,
        choices=URGENCY_CHOICES,
        default=MEDIUM
    )
    contact_person = models.CharField(max_length=150, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    is_fulfilled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hospital.name} needs {self.units_needed} units of {self.blood_type_needed}"


class BloodRequestComment(models.Model):
    request = models.ForeignKey(
        BloodRequest,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blood_request_comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.request}"
    
class BloodDonationEvent(models.Model):
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name='events'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='blood_donation_events'
    )
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='blood_donation_events',
        blank=True
    )

    def __str__(self):
        return f"{self.title} at {self.hospital.name} ({self.start_datetime} - {self.end_datetime})"

