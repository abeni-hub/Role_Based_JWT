from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class User(AbstractUser):
    ROLE_CHOICES = [
        ('receptionist', 'Receptionist'),
        ('nurse', 'Nurse'),
        ('doctor', 'Doctor'),
        ('laboratorist', 'Laboratorist'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='receptionist')

    def __str__(self):
        return f"{self.username} - {self.role}"

User = get_user_model()

class Patient(models.Model):
    receptionist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'receptionist'})
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="registered_patients")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

