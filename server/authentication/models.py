from django.db import models
from django.contrib.auth.models import AbstractUser

class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return f"{self.name}, {self.province}"

    
class Location(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        unique_together = ('name', 'district')

    def __str__(self):
        return f"{self.district.name}, {self.name}"


A_POSITIVE = 'A+'
A_NEGATIVE = 'A-'
B_POSITIVE = 'B+'
B_NEGATIVE = 'B-'
AB_POSITIVE = 'AB+'
AB_NEGATIVE = 'AB-'
O_POSITIVE = 'O+'
O_NEGATIVE = 'O-'

BLOOD_TYPE_CHOICES = [
    (A_POSITIVE, A_POSITIVE),
    (A_NEGATIVE, A_NEGATIVE),
    (B_POSITIVE, B_POSITIVE),
    (B_NEGATIVE, B_NEGATIVE),
    (AB_POSITIVE, AB_POSITIVE),
    (AB_NEGATIVE, AB_NEGATIVE),
    (O_POSITIVE, O_POSITIVE),
    (O_NEGATIVE, O_NEGATIVE),
]

# ! Custom User Model 
class User(AbstractUser):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    email=models.EmailField(unique=True)
    blood_type = models.CharField(
        max_length=3,
        choices=BLOOD_TYPE_CHOICES,
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        Location, 
        on_delete=models.DO_NOTHING,
        related_name='users'
    )
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username']


    def __str__(self) -> str:
        return self.username
    
