# dashboard/urls.py

from django.urls import path
from . import views

# urlpatterns adalah daftar URL yang akan diarahkan ke fungsi view di views.py
urlpatterns = [
    path('deteksi/', views.deteksi, name='deteksi'),  # Rute untuk halaman deteksi
    path('pola-makan/', views.pola_makan, name='pola-makan'),  # Rute untuk halaman pola makan
    path('logout/', views.logout_view, name='logout'),  # Rute untuk proses logout pengguna
    path('result/', views.result, name='result'),  # Rute untuk menampilkan hasil deteksi
]
