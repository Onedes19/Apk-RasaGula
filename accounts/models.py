# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Model kustom untuk user
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (  # Opsi tipe user
        ('admin', 'Admin'),
        ('client', 'Klien'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')  # Field tipe user
    username = models.CharField(max_length=20, unique=True)  # Username harus unik
    email = models.EmailField(max_length=30, unique=True)  # Email harus unik
    password = models.CharField(max_length=128, default='default_password') # Field untuk hash password

    def __str__(self):  # Representasi string model
        return self.username

# Model untuk menyimpan kode verifikasi email
class EmailVerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Relasi ke CustomUser
    code = models.CharField(max_length=6)  # Kode verifikasi
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp pembuatan

