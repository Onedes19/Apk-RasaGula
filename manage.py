#!/usr/bin/env python
"""Utilitas baris perintah Django untuk tugas administratif."""
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Fungsi utama untuk menjalankan tugas administratif Django
def main():
    """Run administrative tasks."""
# Mengatur variabel lingkungan untuk menunjuk ke file pengaturan proyek Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rasagula.settings')
    try:
# Mengimpor fungsi untuk menjalankan perintah dari baris perintah Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
# Menjalankan perintah berdasarkan argumen yang diberikan melalui baris perintah
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
