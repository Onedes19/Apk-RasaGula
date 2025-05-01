# rasagula/wsgi.py

"""
WSGI config for Diabetes Detection Application.

This file configures the Web Server Gateway Interface (WSGI) for the project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Mengatur variabel lingkungan untuk pengaturan Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rasagula.settings')

# Mendapatkan aplikasi WSGI Django
application = get_wsgi_application()
