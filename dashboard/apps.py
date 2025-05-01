# dashboard/apps.py

from django.apps import AppConfig

# Konfigurasi untuk aplikasi 'dashboard'
class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Tipe primary key default untuk model di aplikasi ini
    name = 'dashboard'  # Nama aplikasi
