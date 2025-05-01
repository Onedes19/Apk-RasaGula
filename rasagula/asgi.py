# rasagula/asgi.py

"""
ASGI config for Diabetes_deteksiion_Application project.

ASGI (Asynchronous Server Gateway Interface) digunakan untuk mendukung komunikasi
asinkron pada aplikasi Django.

Dokumentasi resmi:
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Menentukan settings module default untuk proyek ini
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rasagula.settings')

# Membuat instance ASGI application
application = get_asgi_application()
