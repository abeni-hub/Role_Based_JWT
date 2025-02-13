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
    STATUS_CHOICES = [
        ('registered', 'Registered'),
        ('waiting_nurse', 'Waiting for Nurse'),
        ('nurse_checkup', 'Under Nurse Checkup'),
        ('waiting_doctor', 'Waiting for Doctor'),
        ('doctor_checkup', 'Under Doctor Checkup'),
        ('completed', 'Completed Treatment'),
    ]
    
    full_name = models.CharField(max_length=200)  # Full Name
    age = models.PositiveIntegerField()  # Age
    sex = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])  # Sex
    phone_no = models.CharField(max_length=15)  # Phone No
    card_no = models.CharField(max_length=50, unique=True)  # Card No
    kebele = models.CharField(max_length=100)  # Kebele
    region = models.CharField(max_length=100)  # Region
    wereda = models.CharField(max_length=100)  # Wereda

    date_of_birth = models.DateField()
    address = models.TextField()
    
    registered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="registered_patients")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='registered')

    def __str__(self):
        return f"{self.full_name} - {self.status}"