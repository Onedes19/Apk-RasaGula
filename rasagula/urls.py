# rasagula/urls.py

"""rasagula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views untuk halaman utama

# Daftar URL aplikasi utama
urlpatterns = [
    path('admin/', admin.site.urls),  # Rute untuk admin panel Django
    path('', views.index, name='home'),  # Rute ke halaman utama (fungsi index)
    path('accounts/', include('accounts.urls')),  # Rute untuk URL terkait akun
    path('dashboard/', include('dashboard.urls')),  # Rute untuk URL dashboard
]
