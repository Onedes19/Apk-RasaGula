# accounts/urls.py

from django.urls import path
from . import views  # Impor views dari aplikasi accounts
from dashboard.views import deteksi  # Impor fungsi deteksi dari aplikasi dashboard

# Daftar URL patterns untuk aplikasi accounts
urlpatterns = [
    # Route untuk otentikasi user
    path('auth/', views.auth_view, name='auth'),  # Endpoint untuk proses otentikasi
    path('register/', views.register_view, name='register'),  # Endpoint untuk pendaftaran user
    path('login/', views.login_view, name='login'),  # Endpoint untuk login user
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Endpoint untuk halaman dashboard
    path('verify_email/<int:user_id>/', views.verify_email_view, name='verify_email'),  # Endpoint untuk verifikasi email
    
    # Route tambahan untuk halaman deteksi
    path('deteksi/', deteksi, name='deteksi'),  # Menghubungkan endpoint deteksi ke fungsi di dashboard.views
]

