# accounts/apps.py

from django.apps import AppConfig

# Konfigurasi untuk aplikasi 'accounts'
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Primary key default untuk model
    name = 'accounts'  # Nama aplikasi
