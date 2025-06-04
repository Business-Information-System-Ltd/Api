from django.db import models
from django.contrib.auth.models import AbstractUser



class ApiKey(models.Model):
    key = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.key

   
class Budget(models.Model):
    Budget_code = models.CharField(max_length=10, unique=True)
    Budget_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Budget_code} - {self.Budget_name}"

class CustomerUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin','admin'),
        ('staff','staff'),
        ('manager','manager'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return self.username